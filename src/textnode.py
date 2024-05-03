# TextNode Class and related functions

from leafnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
	
	def __init__(self, text, text_type, url=None) -> None:
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, value) -> bool:
		text_same = self.text == value.text
		text_type_same = self.text_type == value.text_type
		url_same = self.url == value.url

		return text_same and text_type_same and url_same
	
	def __repr__(self) -> str:
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
	

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
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
