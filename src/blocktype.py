import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(s: str) -> BlockType:
    if (
        s.startswith("#")
        or s.startswith("##")
        or s.startswith("###")
f       or s.startswith("####")
    ):
        return BlockType.PARAGRAPH

    if s.startswith("```") and s.endswith("```"):
        return BlockType.CODE

    if s.startswith(">"):
        return BlockType.QUOTE

    if s.startswith("-"):
        return BlockType.UNORDERED_LIST

    line = re.compile(r"^(\d+)\. ")
    match = line.match(s)
    if match:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
