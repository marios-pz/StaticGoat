from enum import Enum, auto


class TextType(Enum):
    TEXT = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    LINK = auto()
    IMAGE = auto()


class TextNodeDelimiter(Enum):
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be an instance of TextType Enum")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            )
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
