import unittest
from page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_missing_title(self):
        with self.assertRaises(ValueError):
            extract_title("No headers here")

    def test_only_h2(self):
        with self.assertRaises(ValueError):
            extract_title("## Subheading")
