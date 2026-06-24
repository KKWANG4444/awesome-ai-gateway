#!/usr/bin/env python3
"""Extract BENCHMARKS.md Part 5 ("Real-world reviews") → data/gateway_reality.json
for the interactive site's "Production reality" tab.

BENCHMARKS.md stays the human-edited source of truth; this lifts its Part 5 table
into JSON — the descriptive cells pre-rendered to HTML (bold + sourced links
preserved) so the static page can show the same dated incident / CVE / acquisition
data the markdown carries, without shipping a markdown renderer to the browser.
`--check` fails CI if the JSON drifts from the markdown.

Stdlib only. Reuses the unit-tested inline renderer from build_compare_html.

Usage:
  python scripts/build_reality.py            # write data/gateway_reality.json
  python scripts/build_reality.py --check    # fail if the JSON is stale (CI)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from build_compare_html import _plain, render_inline

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "BENCHMARKS.md"
OUT = ROOT / "data" / "gateway_reality.json"
PART5_ANCHOR = "BENCHMARKS.md#part-5--real-world-reviews-what-production-users-report"


def extract_part5_table(md: str) -> list[list[str]]:
    """Return the Part 5 GFM table as rows of trimmed cell strings (header +
    separator + body). Raises if the heading or table is missing (fail loud)."""
    lines = md.splitlines()
    start = next((i for i, l in enumerate(lines) if l.strip().startswith("## Part 5")), None)
    if start is None:
        raise ValueError("BENCHMARKS.md: '## Part 5' heading not found")
    i = start + 1
    table: list[str] = []
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            while i < len(lines) and lines[i].strip().startswith("|"):
                table.append(lines[i].strip())
                i += 1
            break
        i += 1
    if len(table) < 3:
        raise ValueError("BENCHMARKS.md: no Part 5 table found after the heading")

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    return [cells(r) for r in table]


def build_rows(md: str) -> list[dict]:
    """Parse the Part 5 table body into row dicts. `gateway` is plain text (for
    filtering/sorting), the three descriptive columns are rendered HTML, and
    `search` is the plain-text concat used by the site's filter box."""
    table = extract_part5_table(md)
    rows = []
    for r in table[2:]:  # skip header + |---| separator
        if len(r) < 4:
            continue
        gateway, praised, gripe, event = r[0], r[1], r[2], r[3]
        rows.append({
            "gateway": _plain(gateway),
            "praised": render_inline(praised),
            "gripe": render_inline(gripe) if gripe and gripe != "—" else "",
            "event": render_inline(event),
            "search": _plain(" ".join([gateway, praised, gripe, event])),
        })
    return rows


def render_json(md: str) -> str:
    payload = {"source": PART5_ANCHOR, "rows": build_rows(md)}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Extract BENCHMARKS Part 5 → data/gateway_reality.json.")
    ap.add_argument("--check", action="store_true", help="fail if the JSON is stale (don't write)")
    a = ap.parse_args(argv)

    md = BENCH.read_text(encoding="utf-8")
    out = render_json(md)
    n = len(build_rows(md))
    if a.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if current != out:
            print("::error::data/gateway_reality.json is stale — run 'python scripts/build_reality.py' "
                  "after editing BENCHMARKS.md Part 5", file=sys.stderr)
            return 1
        print(f"gateway_reality.json up to date ({n} rows)")
        return 0
    OUT.write_text(out, encoding="utf-8")
    print(f"wrote data/gateway_reality.json ({n} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
