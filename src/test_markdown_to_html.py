import unittest
from markdown_to_html import *

class TestMarkdown_To_Html(unittest.TestCase):
	def test(self):
		blocks = """This frog is on mars: ![Frog on mars](https://api.google.com/frogmars)

		**Look at what is to see!**
		
		whereas this frog is in a board room. ![Frog in suit](https://api.google.com/frogsuit)"""

		html = markdown_to_html_node(blocks)
	