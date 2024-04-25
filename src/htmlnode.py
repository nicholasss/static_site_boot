# HTMLNode class

class HTMLNode:

	def __init__(self, tag=None, value=None, children=None, props=None) -> None:
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError
	
	def props_to_html(self) -> str:
		#TODO: need to test this
  
		html = ""
		for prop, value in self.props:
			html += f"{prop}=\"{value}\""

			if self.props[1] != None:
				html += " "
		
		return html

	def __repr__(self) -> str:
		#TODO: need to test this

		tag = self.tag
		value = self.value

		return f"<{tag}>{value}</{tag}>"