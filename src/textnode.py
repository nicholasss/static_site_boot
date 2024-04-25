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

		