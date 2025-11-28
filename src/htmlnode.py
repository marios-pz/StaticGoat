from __future__ import annotations

from textnode import TextNode, TextType


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] = None,
        props: dict[str, str] = None,
    ):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] = children if children is not None else []
        self.props: dict[str, str] = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        props = f" {self.props_to_html()}" if self.props else ""
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None:
            raise ValueError("Children must be provided.")
        self.tag = tag
        self.children = children
        self.props = props
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        props_str = self.props_to_html()

        open_tag = f"<{self.tag}{props_str}>"
        close_tag = f"</{self.tag}>"

        html_str = f"{open_tag}"

        for child in self.children:
            html_str += child.to_html()

        html_str += close_tag
        return html_str


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                text_node.url = ""
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            if text_node.url is None:
                text_node.url = ""
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise Exception(f"Unknown TextNode type {text_node.text_type}")
