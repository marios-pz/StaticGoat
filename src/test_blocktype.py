import unittest

from blocktype import BlockType, block_to_block_type


class TestBlocktype(unittest.TestCase):

    def test_block_to_blocktype_paragraph(self):
        pass

    def test_block_to_blocktype_heading(self):
        a = [
            "# amogus",
            "## amogus",
            "### amogus",
            "#### amogus",
        ]

        for item in a:
            self.assertEqual(block_to_block_type(item), BlockType.PARAGRAPH)

    def test_block_to_blocktype_code(self):
        pass

    def test_block_to_blocktype_quote(self):
        pass

    def test_block_to_blocktype_unordered_list(self):
        pass

    def test_block_to_blocktype_ordered_list(self):
        pass
