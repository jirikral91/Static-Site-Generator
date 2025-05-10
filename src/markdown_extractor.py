import re

def extract_markdown_images(text):
    """
    Extrahuje obrázky z markdown textu.
    Vrací seznam dvojic (alt text, URL).
    """
    pattern = r"!\[([^\[\]]*)\]\(([^()]+|[^()]*\([^()]*\)[^()]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Extrahuje odkazy z markdown textu.
    Vrací seznam dvojic (anchor text, URL).
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^()]+|[^()]*\([^()]*\)[^()]*)\)"
    matches = re.findall(pattern, text)
    return matches

