import unittest
from textnode import *
from inline_markdown import *


class TestInline_Markdown(unittest.TestCase):
	def test_split_nodes_delimit(self):
		node_array1 = [
			TextNode("Pizza is looking ", text_type_text),
			TextNode("**GOOD**", text_type_bold),
			TextNode(" right this second.", text_type_text)
		]
		processed_array = split_nodes_delimiter([node_array1[0]], None, text_type_text)
		processed_array += split_nodes_delimiter([node_array1[1]], "**", text_type_bold)
		processed_array += split_nodes_delimiter([node_array1[2]], None, text_type_text)

		self.assertEqual(processed_array[1].text_type, text_type_bold)
		self.assertEqual(processed_array[1].text, "GOOD")
		self.assertEqual(processed_array[0].text_type, text_type_text)
	
	def test_htmlnode_delimit(self):
		pass

	# TODO write tests for extracting markdown urls and images