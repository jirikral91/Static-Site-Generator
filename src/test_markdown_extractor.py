import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):

    def test_extract_markdown_images_single(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "![image1](https://img1.com) and ![image2](https://img2.com)"
        matches = extract_markdown_images(text)
        expected = [
            ("image1", "https://img1.com"),
            ("image2", "https://img2.com")
        ]
        self.assertListEqual(expected, matches)

    def test_extract_markdown_links_single(self):
        text = "This is a [link](https://www.example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://www.example.com")], matches)

    def test_extract_markdown_links_multiple(self):
        text = "[Google](https://google.com) and [GitHub](https://github.com)"
        matches = extract_markdown_links(text)
        expected = [
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com")
        ]
        self.assertListEqual(expected, matches)

    def test_no_images(self):
        text = "This text has no images."
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_no_links(self):
        text = "This text has no links."
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_image_with_special_characters(self):
        text = "Check this ![image](https://img.com/path/to/image_(1).png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://img.com/path/to/image_(1).png")], matches)

    def test_link_with_special_characters(self):
        text = "Visit [example](https://www.example.com/path_(1))"
        matches = extract_markdown_links(text)
        self.assertListEqual([("example", "https://www.example.com/path_(1)")], matches)

if __name__ == "__main__":
    unittest.main()
