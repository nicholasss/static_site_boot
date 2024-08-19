import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
	def test_to_html(self):
		node1 = HTMLNode("p", "This is a sample paragraph.", props={"href": "https://www.google.com"})
		
		self.assertEqual(node1.props_to_html(), 'href="https://www.google.com"')


class TestLeafNode(unittest.TestCase):
	def test_to_html(self):
		node1 = LeafNode("p", "This is a paragraph.")
		node2 = LeafNode("a", "Click me!", {"href": "https://www.apple.com"})

		self.assertEqual(node1.to_html(), "<p>This is a paragraph.</p>")
		self.assertEqual(node2.props_to_html(), 'href="https://www.apple.com"')


class TestParentNode(unittest.TestCase):
	def test_to_html(self):

		header = LeafNode("h1", "New Products!")
		child1 = LeafNode("b", "This is a great deal!")
		child2 = LeafNode(None, "What an amazing value!")

		para = ParentNode("p", [child1, child2])
		body = ParentNode("body", [header, para])

		self.assertTrue("</body>" in body.to_html())
		self.assertTrue("</p>" in para.to_html())
		self.assertTrue("<b>" in body.to_html())

	def test_class_errors(self):

		# Parent class, no children
		with self.assertRaises(ValueError):
			para = ParentNode("p")

		# Parent class, no tag
		child1 = LeafNode("b", "This is a great deal!")
		child2 = LeafNode(None, "What an amazing value!")

		with self.assertRaises(ValueError):
			body = ParentNode(None, [child1, child2])
