# Ch 4 Part 3: Block to HTML

# Take a given block of markdown and convert it to an HTML Node
# This is where all of the previous parts come together to create HTML

from block_markdown import *
from htmlnode import *


DEBUG_PRINT = True

# ================================
# Block Types to HTML Node
# ================================

	# TODO: convert to functional logic

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
	heading_node = HTMLNode(f'h{heading_count}', heading_raw)
	return heading_node


# Code - ' ```code``` `
def code_block(code_string: str):
	code_raw = code_string.strip("```")
	code_node = HTMLNode('code', code_raw)
	return code_node

# Quote - '> quote' on multiple lines
def quote_block(quote_string: str):
	quote_lines = quote_string.splitlines()
	raw_lines = []
	for line in quote_lines:
		raw_lines.append(line[2:])
	lines = "\n".join(raw_lines)
	quote_node = HTMLNode('blockquote', lines)
	return quote_node

# Unordered List - '- ' or '* ' on multiple lines
def ul_block(ul_string: str):
	ul_lines = ul_string.splitlines()
	raw_lines = []
	for line in ul_lines:
		raw_lines.append(line[2:])
	
	node_list = []
	for line in raw_lines:
		node_list.append(HTMLNode('li', line))

	ul_node = HTMLNode('ul', children=node_list)
	return ul_node

# Ordered List - '1. ' on multiple lines (ascending)
def ol_block(ol_string: str):
	ol_lines = ol_string.splitlines()
	raw_lines = []
	for line in ol_lines:
		raw_lines.append(line[3:])
	
	node_list = []
	for line in raw_lines:
		node_list.append(HTMLNode('li', line))
	
	ol_node = HTMLNode('ol', children=node_list)
	return ol_node

# Paragraph
# <p></p>
def paragraph_block(para_string: str):
	return HTMLNode('p', para_string)


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

		elif block_type == bt_code:
			html_list.append(code_block(block))

		elif block_type == bt_quote:
			html_list.append(quote_block(block))

		elif block_type == bt_ulist:
			html_list.append(ul_block(block))

		elif block_type == bt_olist:
			html_list.append(ol_block(block))

		elif block_type == bt_paragraph:
			html_list.append(paragraph_block(block))

	html = HTMLNode("div", children=html_list)

	return html

