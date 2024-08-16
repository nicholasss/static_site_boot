# Ch 4 Part 3: Block to HTML

# Take a given block of markdown and convert it to an HTML Node
# This is where all of the previous parts come together to create HTML

from block_markdown import *
from htmlnode import *


DEBUG_PRINT = True

# ================================
# Block Types to HTML Node
# ================================

# Heading - '# ' --> '###### '
def heading_block(block_string: str):
	heading_count = 0
	for char in block_string:
		if char == "#":
			heading_count += 1
		if char == " ":
			break

	string_start = heading_count + 1
	heading_raw = block_string[string_start:]

	if DEBUG_PRINT:
		print(heading_raw)

	heading_node = HTMLNode(f'h{heading_count}', heading_raw)
	return heading_node


# Code - ' ```code``` `

# Quote - '> quote' on multiple lines

# Unordered List - '- ' or '* ' on multiple lines

# Ordered List - '1. ' on multiple lines (ascending)

# Paragraph


# ================================
# Conversion Function
# ================================

def markdown_to_html_node(markdown: str):

	markdown_blocks = markdown_to_blocks(markdown)
	if DEBUG_PRINT:
		print(markdown_blocks)

	html_list = []
	for block in markdown_blocks:
		block_type = block_to_block_type(block)

		if block_type == bt_heading:
			html_list.append(heading_block(block))

	html = HTMLNode("div", children=html_list)

	return html

