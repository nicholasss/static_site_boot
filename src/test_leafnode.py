import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def testLeafs(self):
		node1 = LeafNode("p", "This is a paragraph.")
		node2 = LeafNode("a", "Click me!", {"href": "https://www.apple.com"})

		print(node2.to_html())

		self.assertEqual(node1.to_html(), "<p>This is a paragraph.</p>")
		self.assertEqual(node2.props_to_html(), 'href="https://www.apple.com"')
		#TODO why does the above fail
		# need to fix both of the above for leaf nodes and html