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

	def test_btb_inline_bold(self):
		md = "This is **bolded** paragraph."
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_paragraph)

	def test_btb_bold_block(self):
		md = "**This is a bolded paragraph.**"
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_paragraph)

	def test_btb_inline_italic(self):
		md = "This is another paragraph with *italic* text."
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_paragraph)

	def test_btb_inline_code(self):
		md = "This here is `code` for you."
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_paragraph)

	def test_btb_code_block(self):
		md = """```new code here wow!
```"""
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_code)

	def test_btb_plain(self):
		md = "Here is some plain text."
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_paragraph)
	
	def test_btb_ulist(self):
		md = """* This is an unordered list
* There are a few things here"""
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_ulist)

	def test_btb_olist(self):
		md = """1. Here is an ordered list
2. There are a specific number of things"""
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_olist)

	def test_btb_quote_block(self):
		md = """> This is,
> a quote section
> wow!"""
		bt = block_to_block_type(md)
		self.assertEqual(bt, bt_quote)
