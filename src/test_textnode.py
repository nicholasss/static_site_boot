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
