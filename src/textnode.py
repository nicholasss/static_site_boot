# TextNode Class and related functions

from htmlnode import *


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

textnode_delimiters = [
	"*",
	"**",
	"`"
]

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
		return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"
	

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


