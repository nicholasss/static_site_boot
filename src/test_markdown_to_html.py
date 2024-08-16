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
		html_one = "<div><h1>Heading One</h1></div>"

		self.assertEqual(markdown_to_html_node(heading_one).to_html(), html_one)