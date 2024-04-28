# HTMLNode class

class HTMLNode:

	def __init__(self, tag=None, value=None, children=None, props=None) -> None:
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		tag = self.tag
		value = self.value

		children = self.children
		if children is None:
			children = ""

		props = self.props_to_html()
		if len(props) > 0:
			props = " " + props

		# print(f"--children-- {type(children)} child type of {tag}")
  
		return f"<{tag}{props}>{value}{children}</{tag}>"
	
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
