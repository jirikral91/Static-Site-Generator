from htmlnode import HTMLNode, LeafNode, ParentNode
from block_type import BlockType, block_to_block_type
from text_to_nodes import text_to_textnodes
from markdown_block_splitter import markdown_to_blocks
from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node


def text_to_children(text):
    """
    Convert text to a list of HTMLNode children using inline markdown parsing.
    """
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]

def handle_paragraph(block):
    """
    Handle paragraph block.
    """
    # Join multiple lines into a single text block
    text = " ".join(block.splitlines()).strip()
    return ParentNode("p", text_to_children(text))


def handle_heading(block):
    """
    Handle heading block.
    """
    level = len(block.split(" ")[0])
    text = block[level + 1:]  # Skip the '#' and space
    return ParentNode(f"h{level}", text_to_children(text))

def handle_codeblock(block):
    """
    Handle code block.
    """
    # Split the block into lines
    lines = block.splitlines()

    # Ensure the block has at least three lines (``` + content + ```)
    if len(lines) >= 3 and lines[0].startswith("```") and lines[-1].startswith("```"):
        # Join lines between markers while preserving newlines
        code_content = "\n".join(lines[1:-1]) + "\n"
        code_node = LeafNode("code", code_content)
        return ParentNode("pre", [code_node])

    # Return empty pre block if structure is invalid
    return ParentNode("pre", [])




def handle_quote(block):
    """
    Handle quote block.
    """
    lines = [line[1:].strip() for line in block.split("\n")]
    quote_text = "\n".join(lines)
    return ParentNode("blockquote", text_to_children(quote_text))

def handle_unordered_list(block):
    """
    Handle unordered list block.
    """
    items = [line[2:].strip() for line in block.split("\n")]
    list_nodes = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ul", list_nodes)

def handle_ordered_list(block):
    """
    Handle ordered list block.
    """
    items = [line.split(". ", 1)[1].strip() for line in block.split("\n")]
    list_nodes = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ol", list_nodes)

def markdown_to_html_node(markdown):
    """
    Convert full markdown text to a single parent HTMLNode.
    """
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(handle_paragraph(block))
        elif block_type == BlockType.HEADING:
            children.append(handle_heading(block))
        elif block_type == BlockType.CODE:
            children.append(handle_codeblock(block))
        elif block_type == BlockType.QUOTE:
            children.append(handle_quote(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(handle_unordered_list(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(handle_ordered_list(block))

    return ParentNode("div", children)
