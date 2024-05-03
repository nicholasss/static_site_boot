import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
	def test_to_html(self):
		node1 = HTMLNode("p", "This is a sample paragraph.", props={"href": "https://www.google.com"})
		
		self.assertEqual(node1.props_to_html(), 'href="https://www.google.com"')