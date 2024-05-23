# Chapter 4, part 1: "split blocks"

# Blocks are seperated by a single blank line

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