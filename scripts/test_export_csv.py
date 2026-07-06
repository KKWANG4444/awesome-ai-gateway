"""Unit tests for export_csv pure functions (no filesystem writes)."""

import unittest

from export_csv import cost_rows, scorecard_rows


class TestCostRows(unittest.TestCase):
    MODELS = [
        {"name": "Cheap", "provider": "B", "scenario_cost": True, "reasoning": False,
         "pricing_usd_per_mtok": {"input": 1.0, "output": 10.0}},
        {"name": "Pricey", "provider": "A", "scenario_cost": True, "reasoning": False,
         "pricing_usd_per_mtok": {"input": 5.0, "output": 25.0}},
        {"name": "NoPrice", "provider": "C", "scenario_cost": True},
        {"name": "Skip", "provider": "D", "scenario_cost": False,
         "pricing_usd_per_mtok": {"input": 1.0, "output": 1.0}},
    ]

    def test_only_priced_flagged_models(self):
        names = [r["model"] for r in cost_rows(self.MODELS)]
        self.assertEqual(set(names), {"Cheap", "Pricey"})

    def test_has_a_column_per_scenario(self):
        row = cost_rows(self.MODELS)[0]
        for key in ("email_usd", "summarize_usd", "coding_usd", "chatbot_usd"):
            self.assertIn(key, row)

    def test_sorted_by_chatbot_cost(self):
        rows = cost_rows(self.MODELS)
        self.assertEqual(rows[0]["model"], "Cheap")


class TestScorecardRows(unittest.TestCase):
    def test_flattens_fields_and_joins_cve(self):
        rows = scorecard_rows([
            {"name": "G", "type": "self-hosted", "self_hosted": True,
             "compliance": 3.0, "markup": "$0", "security": 2.5, "stability": 4.0,
             "observability": 5.0, "cve": ["CVE-1", "CVE-2"]},
        ])
        self.assertEqual(rows[0]["gateway"], "G")
        self.assertEqual(rows[0]["cve"], "CVE-1; CVE-2")
        self.assertEqual(rows[0]["observability"], 5.0)

    def test_missing_cve_is_empty(self):
        rows = scorecard_rows([
            {"name": "G", "type": "hosted", "self_hosted": False,
             "compliance": 4.0, "markup": "0%", "security": 4.0, "stability": 4.0},
        ])
        self.assertEqual(rows[0]["cve"], "")

    def test_missing_observability_is_empty(self):
        rows = scorecard_rows([
            {"name": "G", "type": "hosted", "self_hosted": False,
             "compliance": 4.0, "markup": "0%", "security": 4.0, "stability": 4.0},
        ])
        self.assertEqual(rows[0]["observability"], "")


if __name__ == "__main__":
    unittest.main()
