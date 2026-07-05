"""Unit tests for make_social_preview.py pure data (no PIL).

Headline invariant (mirrors test_make_landscape): the card must not advertise a
gateway the README doesn't carry, and it must stay the GitHub-social 1280x640.
The rendering path (`render`) imports Pillow and is intentionally NOT exercised
here — Pillow is absent on the CI runner.
"""

import unittest
from pathlib import Path

from make_social_preview import H, MARK_COLOR, TABLE, W

README = Path(__file__).resolve().parent.parent / "README.md"


class TestSocialPreviewData(unittest.TestCase):
    def test_dimensions_are_github_social(self):
        self.assertEqual((W, H), (1280, 640))

    def test_table_shape(self):
        self.assertEqual(len(TABLE), 6)
        for row in TABLE:
            # name, stars, + four capability marks
            self.assertEqual(len(row), 6)
            self.assertTrue(row[0].strip())

    def test_marks_have_known_colors(self):
        for _name, _stars, *marks in TABLE:
            for m in marks:
                self.assertIn(m, MARK_COLOR)

    def test_no_drift_every_named_gateway_is_in_readme(self):
        readme = README.read_text(encoding="utf-8")
        missing = [name for name, *_ in TABLE if name not in readme]
        self.assertEqual(missing, [], f"card names not found in README: {missing}")


if __name__ == "__main__":
    unittest.main()
