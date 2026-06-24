"""Unit tests for build_reality.py pure logic (no filesystem writes)."""

import unittest

from build_reality import build_rows, extract_part5_table

SAMPLE = """\
## Part 4 — Scorecard

Some prose.

## Part 5 — Real-world reviews

Intro paragraph with a [link](#part-4).

| Gateway | Praised for | Recurring gripe | Dated event worth knowing |
|---|---|---|---|
| **LiteLLM** | Breadth | Latency at high RPS | ⚠️ **CVE (Mar 2026)** backdoored — [Trend Micro](https://x.com/a) |
| **TensorZero** | Ambitious OSS | — | ⚠️ **Archived June 2026** — [GitHub](https://github.com/t/t) |

> How to read this: a blockquote, not a row.

## Methodology
"""


class TestExtract(unittest.TestCase):
    def test_locates_table_after_part5(self):
        table = extract_part5_table(SAMPLE)
        self.assertEqual(table[0], ["Gateway", "Praised for", "Recurring gripe", "Dated event worth knowing"])
        self.assertEqual(len(table), 4)  # header + separator + 2 rows
        self.assertEqual(table[2][0], "**LiteLLM**")

    def test_raises_without_part5(self):
        with self.assertRaises(ValueError):
            extract_part5_table("# No part five here\n\njust text")

    def test_raises_without_table(self):
        with self.assertRaises(ValueError):
            extract_part5_table("## Part 5 — Reviews\n\nprose but no table\n\n## Next")


class TestBuildRows(unittest.TestCase):
    def setUp(self):
        self.rows = build_rows(SAMPLE)

    def test_two_rows(self):
        self.assertEqual(len(self.rows), 2)

    def test_gateway_is_plain_text(self):
        self.assertEqual(self.rows[0]["gateway"], "LiteLLM")
        self.assertEqual(self.rows[1]["gateway"], "TensorZero")

    def test_descriptive_cells_are_rendered_html(self):
        ev = self.rows[0]["event"]
        self.assertIn("<strong>CVE (Mar 2026)</strong>", ev)
        self.assertIn('<a href="https://x.com/a">Trend Micro</a>', ev)

    def test_dash_gripe_becomes_empty(self):
        self.assertEqual(self.rows[1]["gripe"], "")

    def test_search_is_plain_concat(self):
        s = self.rows[0]["search"]
        self.assertIn("LiteLLM", s)
        self.assertIn("Trend Micro", s)
        self.assertNotIn("**", s)
        self.assertNotIn("<a", s)

    def test_no_markdown_artifacts_in_html_cells(self):
        for r in self.rows:
            for k in ("praised", "gripe", "event"):
                self.assertNotIn("**", r[k])
                self.assertNotIn("](", r[k])


if __name__ == "__main__":
    unittest.main()
