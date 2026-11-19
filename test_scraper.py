"""Offline parser checks. The fixture is checked in; nothing is downloaded."""
import unittest
from pathlib import Path

from scraper import BASE_URL, get_next_page_url, parse_stories

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "hn_frontpage.html"


class ParseStoriesTests(unittest.TestCase):
    def setUp(self):
        self.html = FIXTURE.read_text(encoding="utf-8")

    def test_extracts_titles_and_links(self):
        stories = parse_stories(self.html)
        self.assertEqual(
            [story["title"] for story in stories],
            [
                "Offline parser keeps the title",
                "Ask HN: How does a saved fixture work?",
                "Third story link stays absolute",
            ],
        )
        self.assertEqual(
            [story["link"] for story in stories],
            [
                "https://example.com/offline-parser",
                BASE_URL + "item?id=1002",
                "https://example.org/third-story",
            ],
        )
        for story in stories:
            self.assertIn("scraped_at", story)
            self.assertTrue(story["scraped_at"])

    def test_more_link(self):
        self.assertEqual(get_next_page_url(self.html), BASE_URL + "news?p=2")


if __name__ == "__main__":
    unittest.main()
