#!/usr/bin/env python3
"""Daily content refresher for awesome-ai-gateway.

Updates, in README.md and README.zh-CN.md:
  1. Star counts inside ``<!--s:owner/repo-->...<!--/s-->`` markers.
  2. The "Recent releases" block between ``<!-- RELEASES:START -->`` and
     ``<!-- RELEASES:END -->`` (latest releases of repos listed in
     data/projects.json).

Also writes data/releases.json for programmatic consumers.

Stdlib only. Uses GITHUB_TOKEN from the environment when present
(unauthenticated requests hit GitHub's 60 req/h limit fast).
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_FILES = [ROOT / "README.md", ROOT / "README.zh-CN.md"]
PROJECTS_FILE = ROOT / "data" / "projects.json"
RELEASES_FILE = ROOT / "data" / "releases.json"

STAR_MARKER_RE = re.compile(r"<!--s:([\w.\-]+/[\w.\-]+)-->.*?<!--/s-->", re.DOTALL)
RELEASES_START = "<!-- RELEASES:START -->"
RELEASES_END = "<!-- RELEASES:END -->"
MAX_RELEASES_SHOWN = 12
API_BASE = "https://api.github.com"


def format_stars(count: int) -> str:
    """Render a star count the way GitHub does: 823, 5.7k, 50.3k."""
    if count < 1000:
        return str(count)
    value = count / 1000
    text = f"{value:.1f}".rstrip("0").rstrip(".")
    return f"{text}k"


def collect_marked_repos(text: str) -> list[str]:
    """Unique owner/repo slugs referenced by star markers, in order."""
    seen: list[str] = []
    for match in STAR_MARKER_RE.finditer(text):
        slug = match.group(1)
        if slug not in seen:
            seen.append(slug)
    return seen


def replace_star_markers(text: str, stars: dict[str, int]) -> str:
    """Rewrite every marker whose repo has a fetched count; keep others as-is."""

    def repl(match: re.Match) -> str:
        slug = match.group(1)
        if slug not in stars:
            return match.group(0)
        return f"<!--s:{slug}-->⭐ {format_stars(stars[slug])}<!--/s-->"

    return STAR_MARKER_RE.sub(repl, text)


def replace_between_markers(text: str, start: str, end: str, body: str) -> str:
    """Replace content between two literal markers (markers stay in place)."""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"markers {start!r}/{end!r} not found")
    return pattern.sub(f"{start}\n{body}\n{end}", text)


def render_releases_block(releases: list[dict]) -> str:
    """Markdown bullets for the releases section, newest first."""
    if not releases:
        return "*No recent releases fetched yet.*"
    lines = []
    for rel in releases[:MAX_RELEASES_SHOWN]:
        date = rel["published_at"][:10]
        title = rel.get("name") or rel["tag"]
        # Collapse whitespace/newlines that some projects put in release names.
        title = " ".join(title.split())
        if len(title) > 80:
            title = title[:77] + "..."
        lines.append(f"- **{date}** · [{rel['repo']} {rel['tag']}]({rel['url']}) — {title}")
    return "\n".join(lines)


def github_get(path: str) -> dict | None:
    request = urllib.request.Request(f"{API_BASE}{path}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("User-Agent", "awesome-ai-gateway-updater")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        print(f"warn: GET {path} -> HTTP {err.code}", file=sys.stderr)
        return None
    except (urllib.error.URLError, TimeoutError) as err:
        print(f"warn: GET {path} -> {err}", file=sys.stderr)
        return None


def fetch_stars(repos: list[str]) -> dict[str, int]:
    stars: dict[str, int] = {}
    for slug in repos:
        data = github_get(f"/repos/{slug}")
        if data and isinstance(data.get("stargazers_count"), int):
            stars[slug] = data["stargazers_count"]
    return stars


def fetch_latest_releases(repos: list[str]) -> list[dict]:
    releases: list[dict] = []
    for slug in repos:
        data = github_get(f"/repos/{slug}/releases/latest")
        if not data or not data.get("published_at"):
            continue
        releases.append(
            {
                "repo": slug,
                "tag": data.get("tag_name", ""),
                "name": data.get("name") or data.get("tag_name", ""),
                "published_at": data["published_at"],
                "url": data.get("html_url", f"https://github.com/{slug}/releases"),
            }
        )
    releases.sort(key=lambda r: r["published_at"], reverse=True)
    return releases


def main() -> int:
    tracked = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))["release_tracked_repos"]

    marked_repos: list[str] = []
    for path in README_FILES:
        for slug in collect_marked_repos(path.read_text(encoding="utf-8")):
            if slug not in marked_repos:
                marked_repos.append(slug)

    print(f"fetching stars for {len(marked_repos)} repos...")
    stars = fetch_stars(marked_repos)
    print(f"fetching latest releases for {len(tracked)} repos...")
    releases = fetch_latest_releases(tracked)

    block = render_releases_block(releases)
    changed_files = []
    for path in README_FILES:
        original = path.read_text(encoding="utf-8")
        updated = replace_star_markers(original, stars)
        updated = replace_between_markers(updated, RELEASES_START, RELEASES_END, block)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_files.append(path.name)

    RELEASES_FILE.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "stars": stars,
                "releases": releases,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"stars fetched: {len(stars)}/{len(marked_repos)}; releases: {len(releases)}")
    print(f"updated: {', '.join(changed_files) if changed_files else 'no README changes'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
