from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
	print("Hello, World!")


def text_node_to_html_node(text_node):
	if text_node.text_type == "text":
		return LeafNode(value=text_node.text)
	elif text_node.text_type == "bold":
		return LeafNode("b", text_node.text)
	elif text_node.text_type == "italic":
		return LeafNode("i", text_node.text)
	elif text_node.text_type == "code":
		return LeafNode("code", text_node.text)
	elif text_node.text_type == "link":
		return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
	elif text_node.text_type == "image":
		return LeafNode("img", props={"src": f"{text_node.url}", "alt": "Default Alt Text"})

	else:
		raise ValueError("Unable to convert to HTMLNode Class.")

if __name__ == "__main__":
	main()

