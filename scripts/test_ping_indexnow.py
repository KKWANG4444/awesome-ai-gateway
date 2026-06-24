#!/usr/bin/env python3
"""Unit tests for ping_indexnow — pure logic only (no network)."""
import tempfile
import unittest
from pathlib import Path

from ping_indexnow import build_payload, extract_urls, find_key, HOST, SITE


SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://cuihuan.github.io/awesome-ai-gateway/</loc></url>
  <url><loc> https://cuihuan.github.io/awesome-ai-gateway/cost-calculator.html </loc>
    <lastmod>2026-06-24</lastmod></url>
  <url><loc>https://cuihuan.github.io/awesome-ai-gateway/</loc></url>
</urlset>"""


class ExtractUrls(unittest.TestCase):
    def test_extracts_and_strips_and_dedupes(self):
        urls = extract_urls(SITEMAP)
        self.assertEqual(
            urls,
            [
                "https://cuihuan.github.io/awesome-ai-gateway/",
                "https://cuihuan.github.io/awesome-ai-gateway/cost-calculator.html",
            ],
        )

    def test_empty_sitemap(self):
        self.assertEqual(extract_urls("<urlset></urlset>"), [])


class BuildPayload(unittest.TestCase):
    def test_shape_and_key_location(self):
        key = "42427bee9e0bf57795019a32621a1fd4"
        urls = ["https://cuihuan.github.io/awesome-ai-gateway/"]
        p = build_payload(key, urls)
        self.assertEqual(p["host"], HOST)
        self.assertEqual(p["key"], key)
        # keyLocation must live under our subpath so IndexNow scopes the key to it
        self.assertEqual(p["keyLocation"], f"{SITE}{key}.txt")
        self.assertTrue(p["keyLocation"].startswith(SITE))
        self.assertEqual(p["urlList"], urls)


class FindKey(unittest.TestCase):
    def test_finds_single_valid_key_file(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            key = "deadbeefcafe1234deadbeefcafe1234"
            (root / f"{key}.txt").write_text(key, encoding="utf-8")
            # a decoy non-key txt that must be ignored
            (root / "robots.txt").write_text("User-agent: *", encoding="utf-8")
            self.assertEqual(find_key(root), key)

    def test_rejects_when_content_mismatches_name(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "abcdef1234567890.txt").write_text("not-the-key", encoding="utf-8")
            with self.assertRaises(SystemExit):
                find_key(root)

    def test_rejects_when_no_key_file(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(SystemExit):
                find_key(Path(d))


if __name__ == "__main__":
    unittest.main()
