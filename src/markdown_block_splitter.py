def markdown_to_blocks(markdown):
    """
    Split markdown text into blocks based on blank lines.
    """
    # Split the markdown text by two or more newlines
    raw_blocks = markdown.split("\n\n")
    # Strip whitespace from each block and filter out empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks

