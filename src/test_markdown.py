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

	def test_block_to_block_type(self):
		markdown2 = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

1. first line
2. second line

```new code here wow!
```

> This is,
> a quote section
> wow!
"""
		blocks2 = markdown2.split("\n\n")
		print(blocks2)
		block_types2 = list(map(lambda block: block_to_block_type(block), blocks2))
		self.assertEqual(block_types2,[
			'paragraph',
			'paragraph',
			'unordered_list',
			'ordered_list',
			'code',
			'quote'
		])

		# Currently block_to_block_types is going through every single letter instead of each individual block
