from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def main():
	# print("Hello, World!")

	# temp testing
	old_node = ["This is a *big* pizza pie."]
	delimit = "*"
	new_node = split_nodes_delimiter(old_node, delimit, text_type_italic)

	print(new_node)


def text_node_to_html_node(text_node: TextNode):
	if text_node.text_type == text_type_text:
		return LeafNode(value=text_node.text)
	elif text_node.text_type == text_type_bold:
		return LeafNode("b", text_node.text)
	elif text_node.text_type == text_type_italic:
		return LeafNode("i", text_node.text)
	elif text_node.text_type == text_type_code:
		return LeafNode("code", text_node.text)
	elif text_node.text_type == text_type_link:
		return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
	elif text_node.text_type == text_type_image:
		return LeafNode("img", props={"src": f"{text_node.url}", "alt": "Default Alt Text"})

	else:
		raise ValueError("Unable to convert to HTMLNode Class.")


# This func supports only a single level of nesting.
# i.e. Cannot process "Oh, the **weather *outside* is frightful**"
#
# Func received markdown formattted strings, and converts to to TextNodes
#
# old_nodes must be array type
#
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []

	for old_node in old_nodes:
		processed_string = ""

		# TODO Test
		# If its not a TextNode, then add, as is.
		if type(old_node) is not TextNode:
			new_nodes.append(old_node)

		# Find the position of words within the string, to use later?
		words = old_node.split()
		for word in words:
			if delimiter in word:
				processed_string += word.lstrip(delimiter).rstrip(delimiter)
			else:
				processed_string += word

		# Complete processing
		new_nodes.append(processed_string)

	if len(new_nodes) is 0:
		return None
	
	final_nodes = []
	for new_node in new_nodes:
		final_nodes.append(TextNode(new_node, text_type))
	
	return final_nodes


if __name__ == "__main__":
	main()

