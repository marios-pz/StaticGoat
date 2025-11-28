import unittest

from splitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestSplitter(unittest.TestCase):

    def test_split_nodes_delimiter_single_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        got = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(got, expected)

    def test_split_nodes_delimiter_multiple_code_blocks(self):
        node = TextNode("Text `code1` middle `code2` end", TextType.TEXT)
        got = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("Text ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" middle ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(" end", TextType.TEXT),
        ]

        self.assertListEqual(got, expected)

    def test_split_nodes_delimiter_no_code_block(self):
        node = TextNode("This is a normal sentence.", TextType.TEXT)
        got = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [TextNode("This is a normal sentence.", TextType.TEXT)]

        self.assertListEqual(got, expected)

    def test_split_nodes_delimiter_only_code(self):
        node = TextNode("`only code`", TextType.TEXT)
        got = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [TextNode("only code", TextType.CODE)]

        self.assertListEqual(got, expected)

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
