from textnode import TextNode, TextType
from markdown_extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for alt_text, url in images:
            # Split text based on the image markdown
            split_text = remaining_text.split(f"![{alt_text}]({url})", 1)
            # Preceding text
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            # Image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            # Update remaining text for next iteration
            remaining_text = split_text[1]

        # Add any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for anchor_text, url in links:
            # Split text based on the link markdown
            split_text = remaining_text.split(f"[{anchor_text}]({url})", 1)
            # Preceding text
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            # Link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            # Update remaining text for next iteration
            remaining_text = split_text[1]

        # Add any remaining text after the last link
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
