# ParentNode class that is parent to the leafnodes

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None) -> None:
		super().__init__(tag, None, children, props)
		if self.tag is None:
			raise ValueError("No Tag provided for ParentNode class")
		if self.children is None:
			raise ValueError("No Children provided for ParentNode class")

	#TODO write test file/class and create a few tests to implement against