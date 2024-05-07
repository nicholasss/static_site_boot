import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node1 = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node1, node2, "FAIL")
        
		node1 = TextNode("Looping Garbage", "italic", "https://www.google.com")
		node2 = TextNode("Looping Garbage", "italic", "https://www.google.com")
		self.assertEqual(node1, node2, "FAIL")

		node1 = TextNode("Granite Heights", "bold")
		node2 = TextNode("Granite Heights", "italics")
		self.assertNotEqual(node1, node2, "FAIL")

		node1 = TextNode("Looping Garbage", "italic", "https://www.google.com")
		node2 = TextNode("Looping Garbage", "italic", "https://www.apple.com")
		self.assertNotEqual(node1, node2, "FAIL")

	def test_split_nodes_delimit(self):
		node_array1 = [
			TextNode("Pizza is looking ", text_type_text),
			TextNode("**GOOD** ", text_type_bold),
			TextNode("right this second.", text_type_text)
		]
		processed_array = split_nodes_delimiter(node_array1, "*", text_type_bold)

		print(processed_array)
	
		# TODO test sending in types that are not TextNode