import unittest

from parentnode import ParentNode
from leafnode import LeafNode


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

