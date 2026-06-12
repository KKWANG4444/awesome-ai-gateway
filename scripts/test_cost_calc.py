"""Unit tests for cost_calc.py pure functions (no filesystem/network)."""

import unittest

from cost_calc import (
    Scenario,
    compute_cost,
    cost_ratio,
    format_cost,
    render_scenario_table,
    replace_between_markers,
    scenario_rows,
)

# $1/1M input, $10/1M output — round numbers make the math checkable by hand.
CHEAP = {"input": 1.0, "output": 10.0}
PRICEY = {"input": 5.0, "output": 25.0}

EMAIL = Scenario("email", "Write a 100K-token report", "写报告", 2_000, 100_000)
CODING = Scenario("coding", "Coding session", "编码会话", 50_000, 20_000, thinking_tokens=30_000)


class TestComputeCost(unittest.TestCase):
    def test_generation_heavy(self):
        # 2k input @ $1/1M = $0.002 ; 100k output @ $10/1M = $1.00
        self.assertAlmostEqual(compute_cost(CHEAP, EMAIL, False), 1.002, places=6)

    def test_reasoning_bills_thinking_as_output(self):
        # input 50k@1 = 0.05 ; output (20k+30k)@10 = 0.50 → 0.55
        self.assertAlmostEqual(compute_cost(CHEAP, CODING, True), 0.55, places=6)

    def test_non_reasoning_ignores_thinking(self):
        # input 50k@1 = 0.05 ; output 20k@10 = 0.20 → 0.25
        self.assertAlmostEqual(compute_cost(CHEAP, CODING, False), 0.25, places=6)


class TestFormatCost(unittest.TestCase):
    def test_sub_dollar_cent_precision(self):
        self.assertEqual(format_cost(0.25), "$0.25")

    def test_small_fraction_keeps_milli(self):
        self.assertEqual(format_cost(0.002), "$0.002")

    def test_mid_range_two_decimals(self):
        self.assertEqual(format_cost(1.002), "$1.00")

    def test_large_rounds_to_dollars(self):
        self.assertEqual(format_cost(1234.5), "$1,234")


class TestScenarioRows(unittest.TestCase):
    MODELS = [
        {"name": "Pricey", "provider": "A", "scenario_cost": True, "pricing_usd_per_mtok": PRICEY},
        {"name": "Cheap", "provider": "B", "scenario_cost": True, "pricing_usd_per_mtok": CHEAP},
        {"name": "Skip", "provider": "C", "scenario_cost": False, "pricing_usd_per_mtok": CHEAP},
        {"name": "NoPrice", "provider": "D", "scenario_cost": True},
    ]

    def test_sorted_cheapest_first_and_filtered(self):
        rows = scenario_rows(self.MODELS, EMAIL)
        self.assertEqual([r["name"] for r in rows], ["Cheap", "Pricey"])

    def test_excludes_unflagged_and_unpriced(self):
        names = {r["name"] for r in scenario_rows(self.MODELS, EMAIL)}
        self.assertNotIn("Skip", names)
        self.assertNotIn("NoPrice", names)


class TestCostRatio(unittest.TestCase):
    def test_ratio(self):
        rows = [{"cost": 1.0}, {"cost": 4.0}, {"cost": 2.0}]
        self.assertAlmostEqual(cost_ratio(rows), 4.0)

    def test_single_row_is_zero(self):
        self.assertEqual(cost_ratio([{"cost": 1.0}]), 0.0)


class TestRenderAndMarkers(unittest.TestCase):
    def test_table_lists_models_and_ratio_note(self):
        models = [
            {"name": "Pricey", "provider": "A", "scenario_cost": True, "pricing_usd_per_mtok": PRICEY},
            {"name": "Cheap", "provider": "B", "scenario_cost": True, "pricing_usd_per_mtok": CHEAP},
        ]
        out = render_scenario_table(models, EMAIL)
        self.assertIn("| 1 | Cheap | B |", out)
        self.assertIn("×", out)  # ratio note present

    def test_zh_render_localizes_caption(self):
        models = [
            {"name": "Pricey", "provider": "A", "scenario_cost": True, "pricing_usd_per_mtok": PRICEY},
            {"name": "Cheap", "provider": "B", "scenario_cost": True, "pricing_usd_per_mtok": CHEAP},
        ]
        out = render_scenario_table(models, EMAIL, lang="zh")
        self.assertIn("写报告", out)  # zh title
        self.assertIn("模型", out)  # zh column header
        self.assertIn("低约", out)  # zh ratio note
        self.assertNotIn("Cheapest", out)

    def test_replace_between_markers(self):
        text = "a\n<!-- COST:x:START -->\nold\n<!-- COST:x:END -->\nb"
        out = replace_between_markers(text, "<!-- COST:x:START -->", "<!-- COST:x:END -->", "new")
        self.assertIn("new", out)
        self.assertNotIn("old", out)

    def test_missing_markers_raise(self):
        with self.assertRaises(ValueError):
            replace_between_markers("nope", "<!-- COST:x:START -->", "<!-- COST:x:END -->", "y")


if __name__ == "__main__":
    unittest.main()
