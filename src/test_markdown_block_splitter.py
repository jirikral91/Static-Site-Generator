import unittest
from markdown_block_splitter import markdown_to_blocks

class TestMarkdownBlockSplitter(unittest.TestCase):

    def test_single_paragraph(self):
        md = "This is a single paragraph without blank lines."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph without blank lines."])

    def test_multiple_paragraphs(self):
        md = """
This is the first paragraph.

This is the second paragraph.

This is the third paragraph.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first paragraph.",
                "This is the second paragraph.",
                "This is the third paragraph.",
            ],
        )

    def test_mixed_content(self):
        md = """
# Heading 1

This is a paragraph with **bold** text.

- Item 1
- Item 2

Another paragraph after the list.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "This is a paragraph with **bold** text.",
                "- Item 1\n- Item 2",
                "Another paragraph after the list.",
            ],
        )

    def test_empty_lines(self):
        md = """
Line one.


Line two with extra blank lines.

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Line one.", "Line two with extra blank lines."])

    def test_markdown_with_indented_lines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
