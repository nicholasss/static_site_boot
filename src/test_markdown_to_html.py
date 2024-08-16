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