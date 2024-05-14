import unittest
from textnode import *
from inline_markdown import *


class TestInline_Markdown(unittest.TestCase):
	def test_split_nodes_delimit(self):
		node_array1 = [TextNode("Pizza is looking **GOOD** tonight.", text_type_text)]
		processed_array = split_nodes_delimiter(node_array1, "**", text_type_bold)
		
		self.assertEqual(processed_array[0], TextNode("Pizza is looking ", text_type_text))
		self.assertEqual(processed_array[1], TextNode("GOOD", text_type_bold))
		self.assertEqual(processed_array[2], TextNode(" tonight.", text_type_text))

	def test_extract_md(self):
		url_md = "Look at this new site: [Apple Inc.](https://www.apple.com)!"
		urls_md = "Here [Facebook](https://www.facebook.com) and [Instagram](https://www.instagram.com) will be merging."
		img_md = "This image is ai generated! ![A frog riding a horse](https://api.google.com/froghorse)"
		imgs_md = "This frog is on mars: ![Frog on mars](https://api.google.com/frogmars), whereas this frog is in a board room. ![Frog in suit](https://api.google.com/frogsuit)"

		self.assertEqual(extract_markdown_url(url_md), [("Apple Inc.", "https://www.apple.com")])
		self.assertEqual(extract_markdown_url(urls_md), [("Facebook", "https://www.facebook.com"), ("Instagram", "https://www.instagram.com")])
		self.assertEqual(extract_markdown_image(img_md), [("A frog riding a horse", "https://api.google.com/froghorse")])
		self.assertEqual(extract_markdown_image(imgs_md), [("Frog on mars", "https://api.google.com/frogmars"), ("Frog in suit", "https://api.google.com/frogsuit")])

	def test_split_md(self):
		url1_md = "Here [Facebook](https://www.facebook.com) and [Instagram](https://www.instagram.com) will be merging."
		url1 = TextNode(url1_md, text_type_text)
		proc_url1 = split_nodes_link([url1])

		url2_md = "Look at this new site, [Apple Inc.](https://www.apple.com)!"
		url2 = TextNode(url2_md, text_type_text)
		proc_url2 = split_nodes_link([url2])

		self.assertEqual(proc_url1[0], TextNode("Here ", text_type_text))
		self.assertEqual(proc_url1[1], TextNode("Facebook", text_type_link, "https://www.facebook.com"))

		self.assertEqual(proc_url2[1], TextNode("Apple Inc.", text_type_link, "https://www.apple.com"))
		self.assertEqual(proc_url2[2], TextNode("!", text_type_text))