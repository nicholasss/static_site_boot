# Chapter 4, part 1: "split blocks"

# Blocks are seperated by a single blank line

bt_paragraph = "paragraph"
bt_heading = "heading"
bt_code = "code"
bt_quote = "quote"
bt_ulist = "unordered_list"
bt_olist = "orderd_list"

def markdown_to_blocks(text: str) -> list[str]:
	"""This function takes in a large text and will return each block as a seperate string type in a list"""
	split_blocks = []
	complete_blocks = []

	split_blocks = text.split("\n\n")
	for block in split_blocks:
		if block == "":
			continue
		else:
			complete_blocks.append(block.strip())
	
	return complete_blocks

def block_to_block_type(block: str) -> str:
	"""This function returns the type of block from a given block string"""
	lines = []
	if "\n" in block:
		lines = block.split("\n")
	else:
		lines = [block]

	# Code Blocks or ```\n```
	if "```" in line[:3] and "```" in line[-3:]:
		return bt_code
	
	# Quote Block or "> " on all lines
	num_lines = len(lines)
	quote_count = 0
	for line in lines:
		if "> " in line[:2]:
			quote_count += 1
	if num_lines == quote_count:
		return bt_quote
	
	# Headings must have 1-6 hashes and a trailing space
	for line in lines:
		# returns on first heading line found
		if "# " in line[:7]:
			return bt_headinggi
		
	
