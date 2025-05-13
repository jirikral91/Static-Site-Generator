import unittest
from textnode import TextNode, TextType
from text_to_nodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_basic_text(self):
        text = "This is simple text."
        nodes = text_to_textnodes(text)
        expected = [TextNode("This is simple text.", TextType.TEXT)]
        self.assertListEqual(expected, nodes)

    def test_text_with_bold(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_with_italic_and_code(self):
        text = "Here is _italic_ and `code` text."
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_with_link_and_image(self):
        text = "Check this [link](https://boot.dev) and ![image](https://img.com/pic.png)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Check this ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://img.com/pic.png"),
        ]
        self.assertListEqual(expected, nodes)

    def test_complex_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(expected, nodes)

if __name__ == "__main__":
    unittest.main()
