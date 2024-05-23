import unittest
from block_markdown import *

class Test_Block_Markdown(unittest.TestCase):
	def test_markdown_to_blocks(self):
		markdown1 = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
		blocks1 = markdown_to_blocks(markdown1)
		self.assertEqual(blocks1, [
			'This is **bolded** paragraph',
			'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
			'* This is a list\n* with items'
		])

	