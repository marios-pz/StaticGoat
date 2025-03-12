import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):

    def test_initialization(self):
        node = HTMLNode(
            tag="div",
            value="Hello World",
            children=[HTMLNode(tag="p", value="A paragraph")],
            props={"class": "my-class", "id": "main"},
        )

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.props, {"class": "my-class", "id": "main"})

    def test_props_to_html(self):
        node = HTMLNode(
            tag="div", value="Hello World", props={"class": "my-class", "id": "main"}
        )

        self.assertEqual(node.props_to_html(), 'class="my-class" id="main"')

    def test_children(self):
        parent_node = HTMLNode(tag="div", value="Parent Node")
        child_node = HTMLNode(tag="p", value="Child Node")

        parent_node.children.append(child_node)

        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "p")
        self.assertEqual(parent_node.children[0].value, "Child Node")


class TestLeafNode(unittest.TestCase):

    def test_leaf_no_tag(self):
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://gothchicks.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://gothchicks.com">Click me!</a>'
        )


class TestParentNode(unittest.TestCase):
    def test_a(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
