# HTMLNode Class and its child classes

class HTMLNode:

	def __init__(self, tag=None, value=None, children=None, props=None) -> None:
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		tag_html = self.tag

		value_html = self.value
		if value_html == None:
			value_html = ""

		# needs to go through a list
		children = self.children
		children_html = ""
		if children is None:
			children_html = ""
		else:
			for child in self.children:
				children_html += child.to_html()

		props_html = self.props_to_html()
		if props_html == None:
			props_html = ""
		elif len(props_html) > 0:
			props_html = " " + props_html
  
		return f"<{tag_html}{props_html}>{value_html}{children_html}</{tag_html}>"
	
	def props_to_html(self) -> str:
		html = ""

		if self.props:
			prop_count = len(self.props)
		else:
			return html

		for key, value in self.props.items():
			html += f"{key}=\"{value}\""
			if prop_count > 1:
				html += " "
				prop_count -= 1
		
		return html
	
	def __repr__(self) -> str:
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


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


class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None) -> None:
		super().__init__(tag, None, children, props)
		if self.tag is None:
			raise ValueError("No Tag provided for ParentNode class")
		if self.children is None:
			raise ValueError("No Children provided for ParentNode class")

	#TODO write test file/class and create a few tests to implement against
	# Assumption is that the Children property is an array
 
	def to_html(self):
		html_string = ""
		html_string += f"<{self.tag}>"
		
		# recursion
		for child in self.children:
			html_string += child.to_html()
  
		html_string += f"</{self.tag}>"
		return html_string
	