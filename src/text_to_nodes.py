from textnode import TextNode, TextType
from markdown_splitter import split_nodes_image, split_nodes_link
from inline_markdown import split_nodes_delimiter

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # types
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # returns list of TextNode objects
    return nodes
