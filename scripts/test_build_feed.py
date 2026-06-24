"""Unit tests for build_feed.py pure logic (no filesystem)."""

import unittest
from xml.dom import minidom

from build_feed import render_feed

RELEASES = [
    {"repo": "a/older", "tag": "v1.0", "name": "v1.0", "published_at": "2026-06-10T00:00:00Z", "url": "https://x/1"},
    {"repo": "b/newer", "tag": "v2.0", "name": "Two", "published_at": "2026-06-20T00:00:00Z", "url": "https://x/2"},
    {"repo": "c/mid", "tag": "v1.5", "name": "v1.5", "published_at": "2026-06-15T00:00:00Z", "url": "https://x/3"},
]


class TestRenderFeed(unittest.TestCase):
    def test_well_formed_xml(self):
        minidom.parseString(render_feed(RELEASES))  # raises if malformed

    def test_newest_first_and_feed_updated_is_latest(self):
        feed = render_feed(RELEASES)
        self.assertLess(feed.index("b/newer"), feed.index("c/mid"))
        self.assertLess(feed.index("c/mid"), feed.index("a/older"))
        # feed-level <updated> (before the first <entry>) is the newest release date
        head = feed.split("<entry>")[0]
        self.assertIn("<updated>2026-06-20T00:00:00Z</updated>", head)

    def test_entry_fields(self):
        feed = render_feed(RELEASES)
        self.assertEqual(feed.count("<entry>"), 3)
        self.assertIn("<title>b/newer v2.0</title>", feed)
        self.assertIn('<link href="https://x/2" />', feed)
        self.assertIn("<id>https://x/2</id>", feed)
        self.assertIn("released Two.", feed)
        self.assertIn('<link rel="self" type="application/atom+xml"', feed)

    def test_skips_incomplete_entries(self):
        feed = render_feed(RELEASES + [{"repo": "no/date"}, {"published_at": "2026-06-30T00:00:00Z"}])
        self.assertEqual(feed.count("<entry>"), 3)  # the two incomplete ones dropped

    def test_xml_escaping(self):
        feed = render_feed([{"repo": "a/b", "tag": "v1<2>&", "name": "x", "published_at": "2026-06-01T00:00:00Z", "url": "https://x?a=1&b=2"}])
        self.assertNotIn("<2>&", feed)
        self.assertIn("&lt;2&gt;&amp;", feed)
        self.assertIn("a=1&amp;b=2", feed)
        minidom.parseString(feed)

    def test_dedup_by_url_keeps_ids_unique(self):
        dup = RELEASES + [{"repo": "z/dup", "tag": "v9", "name": "dup", "published_at": "2026-06-25T00:00:00Z", "url": "https://x/2"}]
        feed = render_feed(dup)
        self.assertEqual(feed.count("<id>https://x/2</id>"), 1)  # the dup url appears once

    def test_empty_is_valid(self):
        feed = render_feed([])
        minidom.parseString(feed)
        self.assertEqual(feed.count("<entry>"), 0)


if __name__ == "__main__":
    unittest.main()
