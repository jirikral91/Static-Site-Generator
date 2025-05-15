import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#   Heading 1   "), "Heading 1")

    def test_no_title(self):
        with self.assertRaises(ValueError):
            extract_title("No heading here")

if __name__ == "__main__":
    unittest.main()
