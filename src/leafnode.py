# leaf node class - html node without any children
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None) -> None:
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError
		if self.tag is None:
			return self.value
		return super().to_html()
		
	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"