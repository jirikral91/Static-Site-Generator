from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise ValueError(f"Neplatná syntaxe: chybí uzavírací '{delimiter}' v textu '{node.text}'")

        for i in range(len(split_text)):
            content = split_text[i]
            if content == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(content, TextType.TEXT))
            else:
                new_nodes.append(TextNode(content, text_type))

    return new_nodes
