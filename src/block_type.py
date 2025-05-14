from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    """
    Determine the block type from the given markdown block.
    """
    # Trim whitespace to avoid detection issues
    block = block.strip()

    # Check for code block (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Check for heading (starts with #)
    if block.startswith("#"):
        return BlockType.HEADING

    # Check for quote (each line starts with >)
    if all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE

    # Check for unordered list (each line starts with - )
    if all(line.startswith("- ") for line in block.splitlines()):
        return BlockType.UNORDERED_LIST

    # Check for ordered list (each line starts with number and dot)
    if all(line.split(". ")[0].isdigit() for line in block.splitlines()):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH
