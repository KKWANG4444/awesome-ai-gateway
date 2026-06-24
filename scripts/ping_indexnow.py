#!/usr/bin/env python3
"""Notify IndexNow (Bing, Yandex, …) that the site's URLs changed.

Why: ~87% of ChatGPT Search citations match Bing's top results, so being in
Bing's index is the precondition for being cited by AI answer engines. IndexNow
is a free push protocol that gets URLs into Bing's crawl queue without waiting
for a recrawl — and without needing a Bing Webmaster Tools account.

The site lives under a subpath of a shared host (cuihuan.github.io), so the key
file sits at the project root and is referenced via ``keyLocation``; IndexNow
scopes a key to URLs at or below the key file's directory, which is exactly our
``/awesome-ai-gateway/`` path.

The key is NOT a secret — it is, by design, published at ``keyLocation``.

Usage:
  python scripts/ping_indexnow.py            # extract sitemap URLs and submit
  python scripts/ping_indexnow.py --dry-run  # print the payload, send nothing
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://cuihuan.github.io/awesome-ai-gateway/"
HOST = "cuihuan.github.io"
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP = ROOT / "sitemap.xml"

# An IndexNow key file is named "<key>.txt" and contains exactly "<key>", where
# the key is 8–128 hex chars. We discover it rather than hard-code it, so the
# committed key file stays the single source of truth.
KEY_FILE_RE = re.compile(r"^[0-9a-fA-F]{8,128}\.txt$")
LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.IGNORECASE)


def find_key(root: Path) -> str:
    """Return the IndexNow key whose key file (``<key>.txt`` == its own content)
    sits at *root*. Raises if there is not exactly one valid key file."""
    candidates = []
    for p in root.glob("*.txt"):
        if not KEY_FILE_RE.match(p.name):
            continue
        stem = p.name[:-4]
        if p.read_text(encoding="utf-8").strip() == stem:
            candidates.append(stem)
    if len(candidates) != 1:
        raise SystemExit(
            f"expected exactly one valid IndexNow key file at {root}, found {candidates}"
        )
    return candidates[0]


def extract_urls(sitemap_xml: str) -> list[str]:
    """All <loc> URLs from a sitemap, de-duplicated and order-preserved."""
    seen: dict[str, None] = {}
    for u in LOC_RE.findall(sitemap_xml):
        seen.setdefault(u.strip(), None)
    return list(seen)


def build_payload(key: str, urls: list[str]) -> dict:
    """The IndexNow JSON body. ``keyLocation`` scopes the key to our subpath."""
    return {
        "host": HOST,
        "key": key,
        "keyLocation": f"{SITE}{key}.txt",
        "urlList": urls,
    }


def submit(payload: dict) -> int:
    """POST the payload to IndexNow; return the HTTP status code."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data, headers={"Content-Type": "application/json; charset=utf-8"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Ping IndexNow with the site's sitemap URLs.")
    ap.add_argument("--dry-run", action="store_true", help="print the payload, send nothing")
    args = ap.parse_args(argv)

    key = find_key(ROOT)
    urls = extract_urls(SITEMAP.read_text(encoding="utf-8"))
    if not urls:
        print("no URLs found in sitemap.xml; nothing to submit")
        return 0
    payload = build_payload(key, urls)

    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return 0

    status = submit(payload)
    # IndexNow returns 200 (accepted) or 202 (accepted, pending validation).
    print(f"IndexNow: submitted {len(urls)} URLs → HTTP {status}")
    return 0 if status in (200, 202) else 1


if __name__ == "__main__":
    sys.exit(main())
