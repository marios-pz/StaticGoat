def markdown_to_blocks(markdown: str):
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]
