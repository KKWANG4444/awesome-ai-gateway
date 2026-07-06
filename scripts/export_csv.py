#!/usr/bin/env python3
"""Export the evaluation data to machine-readable CSV companions.

Writes data/cost_table.csv (every model × scenario cost, from the unit-tested
cost engine) and data/gateways_scorecard.csv (from gateways_eval.json). The
point is a queryable, CC0 data surface — the "data is the moat" move that
high-star lists (prompts.chat, awesome-selfhosted) use. Stdlib only.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from cost_calc import MODELS_FILE, SCENARIOS, compute_cost

ROOT = Path(__file__).resolve().parent.parent
GATEWAYS_FILE = ROOT / "data" / "gateways_eval.json"
COST_CSV = ROOT / "data" / "cost_table.csv"
SCORECARD_CSV = ROOT / "data" / "gateways_scorecard.csv"


def cost_rows(models: list[dict]) -> list[dict]:
    """One row per priced model with a column per scenario."""
    rows = []
    for m in models:
        p = m.get("pricing_usd_per_mtok")
        if not (m.get("scenario_cost") and p):
            continue
        row = {"model": m["name"], "provider": m["provider"],
               "input_per_mtok": p["input"], "output_per_mtok": p["output"]}
        for s in SCENARIOS:
            row[f"{s.id}_usd"] = round(compute_cost(p, s, m.get("reasoning", False)), 4)
        rows.append(row)
    rows.sort(key=lambda r: r["chatbot_usd"])
    return rows


def scorecard_rows(gateways: list[dict]) -> list[dict]:
    return [
        {
            "gateway": g["name"], "type": g["type"], "self_hosted": g["self_hosted"],
            "compliance": g["compliance"], "markup": g["markup"],
            "security": g["security"], "stability": g["stability"],
            "observability": g.get("observability", ""),
            "cve": "; ".join(g.get("cve", [])),
        }
        for g in gateways
    ]


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    models = json.loads(MODELS_FILE.read_text(encoding="utf-8"))["models"]
    gateways = json.loads(GATEWAYS_FILE.read_text(encoding="utf-8"))["gateways"]
    write_csv(COST_CSV, cost_rows(models))
    write_csv(SCORECARD_CSV, scorecard_rows(gateways))
    print(f"wrote {COST_CSV.name} and {SCORECARD_CSV.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
