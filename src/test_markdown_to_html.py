import unittest
from markdown_to_html import *

class TestMarkdown_To_Html(unittest.TestCase):
	def test(self):
		blocks = """# Heading One

### Heading Three

**Look at what is to see!**

```This is some code```"""

		html = markdown_to_html_node(blocks)
	
		goal_html = """<h1>Heading One</h1>
<h3>Heading Three</h3>
<p><b>Look at what is to see!</b></p>
<p>whereas this frog is in a board room. <img src="https://api.google.com/frogsuit" alt="Frog in suit"></p>
<code>This is some code</code>"""
		self.assertEqual(html, goal_html)