import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
	def test_props(self):

		header = LeafNode("h1", "New Products!")
		child1 = LeafNode("b", "This is a great deal!")
		child2 = LeafNode(None, "What an amazing value!")

		para = ParentNode("p", [child1, child2])

		body = ParentNode("body", [header, para])

		# print(para.to_html())
		# print(body.to_html())

		# self.assertIn("</body>", body)
		# self.assertIn("</p>", para)
		# self.assertIn("<b>", body)

