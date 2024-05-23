# Chapter 4, part 1: "split blocks"

# Blocks are seperated by a single blank line

def markdown_to_blocks(text: str) -> list[str]:
	"""This function takes in a large text and will return each block as a seperate string type in a list"""
	return text.split("\n\n")
