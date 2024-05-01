from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
	test_textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")

	print(test_textnode)

	test_htmlnode = HTMLNode("p", "This is a sample paragraph.", props={"href": "https://www.google.com"})
	print(test_htmlnode)

	print("\n")

	test2_htmlnode = HTMLNode("h1", "Great News!", children=test_htmlnode)
	print(test2_htmlnode)

	test1_leafnode = LeafNode("h1", "Subject Header")
	print(test1_leafnode.to_html())

if __name__ == "__main__":
	main()

