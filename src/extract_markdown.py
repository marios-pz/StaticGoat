import re
from typing import List, Tuple


def extract_markdown_images(text: str) -> List[Tuple[str | str]]:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)


def extract_markdown_links(text: str) -> List[Tuple[str | str]]:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)
