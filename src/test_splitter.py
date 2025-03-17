import unittest

from splitter import split_nodes_delimiter
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
