#!/usr/bin/env python3
"""Flag listed gateways that have gone stale but aren't labeled as such.

The list's promise (CONTRIBUTING criterion 3) is: a project is "active within the
last 12 months — or it is historically significant and explicitly labeled stale".
This keeps that promise *mechanical* instead of relying on the maintainer noticing.

For every release-tracked repo it checks the GitHub `archived` flag and `pushed_at`
against a 12-month window, then cross-references the README so it only surfaces the
ACTIONABLE cases — repos that are stale/archived but do NOT already carry the house
stale marker (a ⚠️ on the entry's line). Repos that are stale *and* already labeled
are fine (the promise being kept) and are listed separately as "ok".

Advisory by design: the maintainer decides label-vs-remove. Runs monthly in CI and
on demand. Exits non-zero only when there is something to act on (unlabeled stale,
or zero repos successfully checked), so a green run with full coverage means the
promise holds.

Usage:
  GITHUB_TOKEN=$(gh auth token) python scripts/check_stale_gateways.py
  python scripts/check_stale_gateways.py --max-age-days 365
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_FILE = ROOT / "data" / "projects.json"
READMES = [ROOT / "README.md", ROOT / "README.zh-CN.md"]
API = "https://api.github.com/repos/"
SLUG_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
DEFAULT_MAX_AGE_DAYS = 365


def load_tracked() -> list[str]:
    """Tracked repos, skipping any malformed slug (typos never reach the network)."""
    slugs = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))["release_tracked_repos"]
    return [s for s in slugs if SLUG_RE.fullmatch(s)]


def github_get(slug: str, token: str | None) -> dict:
    req = urllib.request.Request(
        API + slug,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "stale-check"},
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}"}
    except (urllib.error.URLError, TimeoutError, OSError) as e:  # pragma: no cover - network
        return {"_error": str(e)}


def classify(meta: dict, now: datetime, max_age_days: int) -> tuple[bool, str]:
    """Pure. Return (is_stale, reason). Never flag on a fetch/parse error (avoid noise)."""
    if meta.get("_error") is not None:
        return (False, "")
    if meta.get("archived"):
        return (True, "archived")
    pushed = meta.get("pushed_at")
    if not pushed:
        return (False, "")
    try:
        dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
    except ValueError:
        return (False, "")
    age = (now - dt).days
    if age > max_age_days:
        return (True, f"no push in {age}d")
    return (False, "")


def is_labeled_stale(readme_text: str, slug: str) -> bool:
    """Pure. Is the entry whose star-marker is `slug` flagged with the house ⚠️ convention?

    We key on the ⚠️ marker, which is the intentional editorial signal the list uses
    for every stale/archived entry — NOT on prose words like "deprecated"/"inactive",
    which legitimately appear in active-project descriptions (e.g. "replaces the
    deprecated v1 proxy"). An entry that is stale-by-data but carries no ⚠️ is exactly
    what we want surfaced — that's the convention not being followed yet.
    """
    needle = f"<!--s:{slug}-->"
    return any(needle in line and "⚠️" in line for line in readme_text.splitlines())


def build_report(
    rows: list[tuple[str, str, bool]], errors: list[str], checked: int
) -> tuple[str, int]:
    """rows: (slug, reason, labeled) for stale repos. Returns (markdown, exit_code).

    exit_code is 1 when there is something to act on: an unlabeled stale entry, or a
    total fetch failure (checked == 0). Transient partial errors are surfaced but do
    not by themselves turn the run red.
    """
    unlabeled = [(s, r) for s, r, lab in rows if not lab]
    labeled = [(s, r) for s, r, lab in rows if lab]
    cov = f"checked {checked} repos" + (f", {len(errors)} could not be fetched" if errors else "")
    out = ["# Stale-gateway check\n"]
    if unlabeled:
        out.append(f"## ⚠️ {len(unlabeled)} stale but UNLABELED — add a ⚠️ label or remove ({cov}):\n")
        out += [f"- **{s}** — {r}" for s, r in unlabeled]
    elif checked == 0:
        out.append("## ❌ Could not check any repos (0 fetched) — coverage failure, re-run.\n")
    elif errors:
        out.append(f"## ✅ No unlabeled stale gateways among the {checked} checked — but coverage is incomplete (see below).\n")
    else:
        out.append(f"## ✅ No unlabeled stale gateways ({cov}) — the 12-month promise holds.\n")
    if labeled:
        out.append(f"\n## ℹ️ {len(labeled)} stale and already labeled (fine):\n")
        out += [f"- {s} — {r}" for s, r in labeled]
    if errors:
        out.append(f"\n## ⚠️ {len(errors)} not checked (coverage incomplete):\n")
        out += [f"- {e}" for e in errors]
    code = 1 if (unlabeled or checked == 0) else 0
    return ("\n".join(out) + "\n", code)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Flag stale-but-unlabeled listed gateways.")
    ap.add_argument("--max-age-days", type=int, default=DEFAULT_MAX_AGE_DAYS)
    args = ap.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN")
    now = datetime.now(timezone.utc)
    readme_text = "\n".join(p.read_text(encoding="utf-8") for p in READMES if p.exists())

    rows: list[tuple[str, str, bool]] = []
    errors: list[str] = []
    checked = 0
    for slug in load_tracked():
        meta = github_get(slug, token)
        if meta.get("_error") is not None:
            errors.append(f"{slug}: {meta['_error']}")
            continue
        checked += 1
        is_stale, reason = classify(meta, now, args.max_age_days)
        if is_stale:
            rows.append((slug, reason, is_labeled_stale(readme_text, slug)))

    report, code = build_report(rows, errors, checked)
    print(report)
    return code


if __name__ == "__main__":
    sys.exit(main())
