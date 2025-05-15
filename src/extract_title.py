def extract_title(markdown):
    """
    Extract the first-level heading from markdown.
    """
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found in the markdown file.")
