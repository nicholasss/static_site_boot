from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
	print("Hello, World!")


# This func supports only a single level of nesting.
# i.e. Cannot process "Oh, the **weather *outside* is frightful**"
#
# Func received markdown formattted strings, and converts to to TextNodes
#
# old_nodes must be array type
#
def split_nodes_delimiter(old_nodes, delimiter: str, text_type: str):
	new_nodes = []

	for old_node in old_nodes:
		processed_words = []

		# TODO Test
		# If its not a TextNode, then add, as is.
		if type(old_node) is not TextNode:
			print(f" --NOT TEXTNODE-- {old_node}")
			new_nodes.append(old_node)

		# Find the position of words within the string, to use later?
		words = old_node.text.split()
		for word in words:
			print(word)
			if delimiter in word:
				processed_words.append(word.lstrip(delimiter).rstrip(delimiter))
			else:
				processed_words.append(word)

		# Complete processing
		processed_string = " ".join(processed_words)
		new_nodes.append(processed_string)

	if len(new_nodes) == 0:
		return None
	
	final_nodes = []
	for new_node in new_nodes:
		print(f" --NEW NODE-- {new_node}")
		final_nodes.append(TextNode(new_node, text_type))
	
	return final_nodes


if __name__ == "__main__":
	main()

