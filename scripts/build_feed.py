#!/usr/bin/env python3
"""Generate feed.xml — an Atom feed of the latest releases from tracked gateways.

The daily-update workflow already collects `data/releases.json` (one latest
release per tracked repo: repo / tag / name / published_at / url) and today only
turns it into README text. This reformats that same data into a subscribable
Atom 1.0 feed — the project's "what's new in the ecosystem" surface — with zero
new data and no fabrication. The feed's <updated> is the newest release date, so
feed.xml only changes when a real release lands (no daily churn).

Stdlib only. The render is pure and unit-tested; only main() touches the disk.

Usage:
  python scripts/build_feed.py            # write feed.xml
  python scripts/build_feed.py --check    # fail if feed.xml is stale (CI)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
RELEASES = ROOT / "data" / "releases.json"
OUT = ROOT / "feed.xml"
SITE = "https://cuihuan.github.io/awesome-ai-gateway/"
FEED_URL = SITE + "feed.xml"
MAX_ENTRIES = 30


def render_feed(releases: list[dict]) -> str:
    """Render an Atom 1.0 feed from release dicts (repo/tag/name/published_at/url).
    Newest first, capped at MAX_ENTRIES. Pure — no I/O."""
    valid = [r for r in releases if r.get("published_at") and r.get("url") and r.get("repo")]
    valid.sort(key=lambda r: r["published_at"], reverse=True)
    valid = valid[:MAX_ENTRIES]
    updated = valid[0]["published_at"] if valid else "1970-01-01T00:00:00Z"

    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        "  <title>Awesome AI Gateway — ecosystem releases</title>",
        "  <subtitle>Latest releases from the AI gateways / LLM proxies tracked by Awesome AI Gateway.</subtitle>",
        f'  <link href="{SITE}" />',
        f'  <link rel="self" type="application/atom+xml" href="{FEED_URL}" />',
        f"  <id>{FEED_URL}</id>",
        f"  <updated>{updated}</updated>",
        "  <author><name>Awesome AI Gateway</name></author>",
    ]
    for r in valid:
        repo = escape(r["repo"])
        tag = escape(str(r.get("tag") or r.get("name") or ""))
        name = escape(str(r.get("name") or r.get("tag") or ""))
        url = escape(r["url"])
        title = f"{repo} {tag}".strip()
        parts += [
            "  <entry>",
            f"    <title>{title}</title>",
            f'    <link href="{url}" />',
            f"    <id>{url}</id>",
            f"    <updated>{escape(r['published_at'])}</updated>",
            f"    <summary>{repo} released {name}.</summary>",
            "  </entry>",
        ]
    parts.append("</feed>")
    return "\n".join(parts) + "\n"


def _load_releases() -> list[dict]:
    data = json.loads(RELEASES.read_text(encoding="utf-8"))
    return data.get("releases", []) if isinstance(data, dict) else []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Generate feed.xml (Atom) from data/releases.json.")
    ap.add_argument("--check", action="store_true", help="fail if feed.xml is stale (don't write)")
    a = ap.parse_args(argv)

    content = render_feed(_load_releases())
    if a.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if current != content:
            print("::error::feed.xml is stale — run 'python scripts/build_feed.py' after data/releases.json changes",
                  file=sys.stderr)
            return 1
        print("feed.xml up to date")
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"wrote feed.xml ({content.count('<entry>')} releases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
