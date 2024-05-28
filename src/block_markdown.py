# Chapter 4, part 1: "split blocks"

# Blocks are seperated by a single blank line

bt_paragraph = "paragraph"
bt_heading = "heading"
bt_code = "code"
bt_quote = "quote"
bt_ulist = "unordered_list"
bt_olist = "ordered_list"

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
	num_lines = len(lines)
	# print(f"--CURRENT--\n{lines}\n")

	# Code Blocks or ```\n```
	if "```" in block[:3] and "```" in block[-3:]:
		return bt_code
	
	# Quote Block or "> " on all lines
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
			return bt_heading
		
	# Unordered list or "* ", "- "
	u_line_count = 0
	for line in lines:
		if "- " in line[:2] or "* " in line[:2]:
			u_line_count += 1
	if u_line_count == num_lines:
		# print(f" -+- found unordered list")
		return bt_ulist
	
	# Ordered list
	o_list_count = 0
	if "1" == block[:1]:
		current_num = 1
		for line in lines:
			if current_num == int(line[:1]): # Is incrementing by one
				o_list_count += 1
			current_num += 1
		if o_list_count == num_lines:
			return bt_olist
		
	# print(f"\n --DEBUG-- Normal Paragraph\n{block}\n======\n")
	return bt_paragraph