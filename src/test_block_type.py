import unittest
from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Subheading"), BlockType.HEADING)

    def test_code_block(self):
        code_block = """```
print("Hello, World!")
```"""
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)

    def test_quote_block(self):
        quote_block = """> This is a quote
> with multiple lines"""
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

    def test_unordered_list(self):
        unordered_list = """- Item 1
- Item 2
- Item 3"""
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ordered_list = """1. First item
2. Second item
3. Third item"""
        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        paragraph = "This is a normal paragraph without any special formatting."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)

    def test_mixed_content(self):
        mixed_content = """1. First item
- Unordered item"""
        self.assertEqual(block_to_block_type(mixed_content), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
