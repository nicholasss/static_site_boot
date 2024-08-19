import unittest
from markdown_to_html import *

class TestMarkdown_To_Html(unittest.TestCase):
# 	def test(self):
# 		blocks = """# Heading One

# ### Heading Three

# **Look at what is to see!**

# ```This is some code```"""

# 		html = markdown_to_html_node(blocks)
	
# 		goal_html = """<h1>Heading One</h1>
# <h3>Heading Three</h3>
# <p><b>Look at what is to see!</b></p>
# <code>This is some code</code>"""
# 		self.assertEqual(html, goal_html)

	def test_heading(self):
		heading_one = "# Heading One"
		html_heading_one = "<div><h1>Heading One</h1></div>"
		self.assertEqual(markdown_to_html_node(heading_one).to_html(), html_heading_one)

		heading_three = "### Heading Three"
		html_heading_three = "<div><h3>Heading Three</h3></div>"
		self.assertEqual(markdown_to_html_node(heading_three).to_html(), html_heading_three)

		heading_five = "##### Heading Five"
		html_heading_five = "<div><h5>Heading Five</h5></div>"
		self.assertEqual(markdown_to_html_node(heading_five).to_html(), html_heading_five)

	def test_code(self):
		code_one = "```Code block```"
		html_code_one = "<div><code>Code block</code></div>"
		self.assertEqual(markdown_to_html_node(code_one).to_html(), html_code_one)

		code_two = """```Code section
Line two
Line three```"""
		html_code_two = """<div><code>Code section
Line two
Line three</code></div>"""
		self.assertEqual(markdown_to_html_node(code_two).to_html(), html_code_two)

	def test_quote(self):
		quote_one = "> Quote section"
		html_quote_one = "<div><blockquote>Quote section</blockquote></div>"
		self.assertEqual(markdown_to_html_node(quote_one).to_html(), html_quote_one)

		quote_two = """> Large quote block
> Second line
> Third line"""
		html_quote_two = """<div><blockquote>Large quote block
Second line
Third line</blockquote></div>"""
		self.assertEqual(markdown_to_html_node(quote_two).to_html(), html_quote_two)

	def test_unordered_list(self):
		ul_list_one = "* List of one"
		html_ul_list_one = "<div><ul><li>List of one</li></ul></div>"
		self.assertEqual(markdown_to_html_node(ul_list_one).to_html(), html_ul_list_one)

		ul_list_two = """* Many list
* Another item"""
		html_ul_list_two = """<div><ul><li>Many list</li><li>Another item</li></ul></div>"""
		self.assertEqual(markdown_to_html_node(ul_list_two).to_html(), html_ul_list_two)

	def test_orderded_list(self):
		ol_list_one = "1. List of one"
		html_ol_list_one = "<div><ol><li>List of one</li></ol></div>"
		self.assertEqual(markdown_to_html_node(ol_list_one).to_html(), html_ol_list_one)

		ol_list_two = """1. Long list
2. Another item"""
		html_ol_list_two = """<div><ol><li>Long list</li><li>Another item</li></ol></div>"""
		self.assertEqual(markdown_to_html_node(ol_list_two).to_html(), html_ol_list_two)