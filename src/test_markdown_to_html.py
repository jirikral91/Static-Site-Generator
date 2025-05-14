import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>" \
                        "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(html, expected_html)

    def test_codeblock(self):
        md = md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(html, expected_html)

    def test_quote(self):
        md = """
> This is a quote
> that spans multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = "<div><blockquote>This is a quote\nthat spans multiple lines</blockquote></div>"
        self.assertEqual(html, expected_html)

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
        self.assertEqual(html, expected_html)

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        self.assertEqual(html, expected_html)

    def test_mixed_content(self):
        md = """
This is a paragraph

1. Ordered item one
2. Ordered item two

- Unordered item one
- Unordered item two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = "<div><p>This is a paragraph</p>" \
                        "<ol><li>Ordered item one</li><li>Ordered item two</li></ol>" \
                        "<ul><li>Unordered item one</li><li>Unordered item two</li></ul></div>"
        self.assertEqual(html, expected_html)

if __name__ == "__main__":
    unittest.main()
