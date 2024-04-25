# TextNode Class

# In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor:

    # self.text - The text content of the node
    # self.text_type - The type of text this node contains, which is just a string like "bold" or "italic"
    # self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

class TextNode:
	
	def __init__(self, text, text_type, url) -> None:
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, value: TextNode) -> bool:
		text_same = self.text == value.text
		text_type_same = self.text_type == value.text_type
		url_same = self.url == value.url

		return text_same and text_type_same and url_same
	
	def __repr__(self) -> str:
		return f"TextNode({self.text}, {self.text_type}, {self.url})"