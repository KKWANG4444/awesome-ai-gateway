"""Unit tests for the pure functions in update_readme.py (no network)."""

import unittest

from update_readme import (
    collect_marked_repos,
    format_stars,
    render_releases_block,
    replace_between_markers,
    replace_star_markers,
)


class TestFormatStars(unittest.TestCase):
    def test_below_thousand_is_plain(self):
        self.assertEqual(format_stars(0), "0")
        self.assertEqual(format_stars(823), "823")

    def test_thousands_get_one_decimal(self):
        self.assertEqual(format_stars(5712), "5.7k")
        self.assertEqual(format_stars(1234), "1.2k")

    def test_round_thousands_drop_decimal(self):
        self.assertEqual(format_stars(50000), "50k")
        self.assertEqual(format_stars(50049), "50k")

    def test_large_counts(self):
        self.assertEqual(format_stars(50349), "50.3k")


class TestStarMarkers(unittest.TestCase):
    SAMPLE = (
        "| [A](https://github.com/o/a) | <!--s:o/a-->⭐ ~1k<!--/s--> |\n"
        "- [B](https://github.com/o/b) <!--s:o/b-->⭐ old<!--/s--> text\n"
        "- [A again](https://github.com/o/a) <!--s:o/a-->⭐ ~1k<!--/s-->\n"
    )

    def test_collect_unique_in_order(self):
        self.assertEqual(collect_marked_repos(self.SAMPLE), ["o/a", "o/b"])

    def test_replace_known_repos(self):
        out = replace_star_markers(self.SAMPLE, {"o/a": 1500, "o/b": 230})
        self.assertIn("<!--s:o/a-->⭐ 1.5k<!--/s-->", out)
        self.assertIn("<!--s:o/b-->⭐ 230<!--/s-->", out)
        self.assertNotIn("old", out)

    def test_unknown_repo_left_untouched(self):
        out = replace_star_markers(self.SAMPLE, {"o/a": 1500})
        self.assertIn("<!--s:o/b-->⭐ old<!--/s-->", out)

    def test_replace_is_idempotent(self):
        once = replace_star_markers(self.SAMPLE, {"o/a": 1500, "o/b": 230})
        twice = replace_star_markers(once, {"o/a": 1500, "o/b": 230})
        self.assertEqual(once, twice)


class TestReplaceBetweenMarkers(unittest.TestCase):
    def test_replaces_content_and_keeps_markers(self):
        text = "head\n<!-- X:START -->\nold\n<!-- X:END -->\ntail"
        out = replace_between_markers(text, "<!-- X:START -->", "<!-- X:END -->", "new")
        self.assertEqual(out, "head\n<!-- X:START -->\nnew\n<!-- X:END -->\ntail")

    def test_missing_markers_raise(self):
        with self.assertRaises(ValueError):
            replace_between_markers("no markers", "<!-- X:START -->", "<!-- X:END -->", "x")


class TestRenderReleases(unittest.TestCase):
    def test_empty_list_renders_placeholder(self):
        self.assertIn("No recent releases", render_releases_block([]))

    def test_renders_date_repo_and_link(self):
        block = render_releases_block(
            [
                {
                    "repo": "o/a",
                    "tag": "v1.2.0",
                    "name": "Big   release\nwith newline",
                    "published_at": "2026-06-10T12:00:00Z",
                    "url": "https://github.com/o/a/releases/tag/v1.2.0",
                }
            ]
        )
        self.assertIn("**2026-06-10**", block)
        self.assertIn("[o/a v1.2.0](https://github.com/o/a/releases/tag/v1.2.0)", block)
        self.assertIn("Big release with newline", block)

    def test_caps_at_twelve_entries(self):
        releases = [
            {
                "repo": f"o/r{i}",
                "tag": "v1",
                "name": "r",
                "published_at": f"2026-06-{i + 1:02d}T00:00:00Z",
                "url": "https://example.com",
            }
            for i in range(20)
        ]
        block = render_releases_block(releases)
        self.assertEqual(block.count("\n") + 1, 12)


if __name__ == "__main__":
    unittest.main()
