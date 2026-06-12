#!/usr/bin/env python3
"""Reproducible LLM cost calculator for the evaluation set.

Reads model pricing from data/models.json and computes the cost of each
benchmark scenario (e.g. "write a 100k-token email") for every model flagged
with ``scenario_cost: true``. Renders markdown tables into BENCHMARKS.md and
BENCHMARKS.zh-CN.md between ``<!-- COST:<id>:START -->`` / ``...:END -->`` markers.

The point is auditability: every published cost cell is recomputed from the
pricing table by this script, never hand-typed. Pricing is USD per 1M tokens.

Stdlib only.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_FILE = ROOT / "data" / "models.json"
DOC_FILES = [ROOT / "BENCHMARKS.md", ROOT / "BENCHMARKS.zh-CN.md"]


@dataclass(frozen=True)
class Scenario:
    """A billable workload. thinking_tokens are billed as output, but only for
    models that emit hidden reasoning tokens (``reasoning: true``)."""

    id: str
    title: str
    title_zh: str
    input_tokens: int
    output_tokens: int
    thinking_tokens: int = 0


# Headline scenarios. Token counts are the published assumptions — keep them
# round and explained in the doc so readers can re-derive every number.
SCENARIOS = [
    Scenario("email", "Write a 100K-token report", "写一封 10 万 token 的报告", 2_000, 100_000),
    Scenario("summarize", "Summarize a 100K-token document", "总结一份 10 万 token 的文档", 100_000, 2_000),
    Scenario("coding", "Coding-agent session", "编码 Agent 会话", 50_000, 20_000, thinking_tokens=30_000),
    Scenario("chatbot", "1M-token chatbot month", "百万 token 聊天机器人月度", 500_000, 500_000),
]

# Per-language captions so the Chinese doc reads natively while sharing one engine.
LABELS = {
    "en": {
        "input": "input", "output": "output",
        "thinking": "+{n:,} thinking for reasoning models",
        "cols": "| # | Model | Provider | Cost |",
        "ratio": "> 📊 Cheapest is **~{r:.0f}×** less than the most expensive for this task.",
        "empty": "*No priced models available.*",
    },
    "zh": {
        "input": "输入", "output": "输出",
        "thinking": "推理模型另计 {n:,} 思考 token",
        "cols": "| # | 模型 | 厂商 | 成本 |",
        "ratio": "> 📊 最便宜的比最贵的低约 **{r:.0f}×**。",
        "empty": "*暂无可计价模型。*",
    },
}


def compute_cost(pricing: dict, scenario: Scenario, is_reasoning: bool) -> float:
    """Cost in USD for one model on one scenario.

    Reasoning models bill their hidden thinking tokens at the output rate;
    non-reasoning models ignore the scenario's thinking_tokens.
    """
    in_rate = pricing["input"]
    out_rate = pricing["output"]
    billed_output = scenario.output_tokens
    if is_reasoning:
        billed_output += scenario.thinking_tokens
    return (scenario.input_tokens / 1_000_000) * in_rate + (
        billed_output / 1_000_000
    ) * out_rate


def format_cost(cost: float) -> str:
    """Human-friendly USD: <$1 to the cent, larger to two sig figures."""
    if cost < 1:
        return f"${cost:.3f}".rstrip("0").rstrip(".") if cost < 0.1 else f"${cost:.2f}"
    if cost < 100:
        return f"${cost:.2f}"
    return f"${cost:,.0f}"


def scenario_rows(models: list[dict], scenario: Scenario) -> list[dict]:
    """Cost rows for the priced models, cheapest first."""
    rows = []
    for m in models:
        pricing = m.get("pricing_usd_per_mtok")
        if not m.get("scenario_cost") or not pricing:
            continue
        cost = compute_cost(pricing, scenario, m.get("reasoning", False))
        rows.append({"name": m["name"], "provider": m["provider"], "cost": cost})
    rows.sort(key=lambda r: r["cost"])
    return rows


def cost_ratio(rows: list[dict]) -> float:
    """Most-expensive / cheapest cost ratio (0 if not computable)."""
    costs = [r["cost"] for r in rows if r["cost"] > 0]
    if len(costs) < 2:
        return 0.0
    return max(costs) / min(costs)


def render_scenario_table(models: list[dict], scenario: Scenario, lang: str = "en") -> str:
    lbl = LABELS.get(lang, LABELS["en"])
    rows = scenario_rows(models, scenario)
    if not rows:
        return lbl["empty"]
    title = scenario.title_zh if lang == "zh" else scenario.title
    annot = f"{lbl['input']} {scenario.input_tokens:,} tok · {lbl['output']} {scenario.output_tokens:,} tok"
    if scenario.thinking_tokens:
        annot += " · " + lbl["thinking"].format(n=scenario.thinking_tokens)
    lines = [f"**{title}** ({annot})", "", lbl["cols"], "|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        lines.append(f"| {i} | {r['name']} | {r['provider']} | {format_cost(r['cost'])} |")
    ratio = cost_ratio(rows)
    if ratio >= 2:
        lines += ["", lbl["ratio"].format(r=ratio)]
    return "\n".join(lines)


def replace_between_markers(text: str, start: str, end: str, body: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"markers {start!r}/{end!r} not found")
    return pattern.sub(f"{start}\n{body}\n{end}", text)


def main() -> int:
    models = json.loads(MODELS_FILE.read_text(encoding="utf-8"))["models"]
    changed = []
    for path in DOC_FILES:
        if not path.exists():
            continue
        lang = "zh" if "zh-CN" in path.name else "en"
        text = original = path.read_text(encoding="utf-8")
        for scenario in SCENARIOS:
            start = f"<!-- COST:{scenario.id}:START -->"
            end = f"<!-- COST:{scenario.id}:END -->"
            if start in text:
                text = replace_between_markers(text, start, end, render_scenario_table(models, scenario, lang))
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(path.name)
    print(f"cost tables refreshed in: {', '.join(changed) if changed else 'no changes'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
