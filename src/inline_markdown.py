# Markdown Functions

from re import findall
from textnode import *


# Extract Markdown Images
# Returns list of tuples with alt text and image urls
def extract_markdown_image(text):
	return findall(r"!\[(.*?)\]\((.*?)\)", text)

# Extract Markdown URLS
# Returns list of tuples with alt text and URLs
def extract_markdown_url(text):
	return findall(r"\[(.*?)\]\((.*?)\)", text)

# Split Nodes Delmitiier
# receive one textnode
#    TextNode("This is **huge** for us!", "text")
# and return several textnodes
#    TextNode("This is ", "text"),
#    TextNode("**huge**", "bold"),
#    TextNode(" for us!", "text")
def split_nodes_delimiter(old_nodes, delimiter: str, text_type: str):
	if len(old_nodes) == 0:
		return []

	new_nodes = []
	for old_node in old_nodes:
		processed_words = []
		has_end_space = old_node.text[-1] == " "

		# If its not a TextNode, then add, as is.
		if type(old_node) is not TextNode:
			# print(f" --NOT TEXTNODE-- {old_node}")
			new_nodes.append(old_node)

		words = old_node.text.split()
		for word in words:

			# print(f" --WORD-- \"{word}\"")
			# print(f" --DELIMITER-- \"{delimiter}\"")
			if delimiter == None or text_type == text_type_text:
				processed_words.append(word)

			elif delimiter in word:
				begin_delimit_found: bool = word[:2] == delimiter
				end_delimit_found: bool = word[-2:] == delimiter
				if not ( begin_delimit_found and end_delimit_found ):
					# print(f" --DELIMIT TEST-- {begin_delimit_found}, {end_delimit_found} in {word}")
					raise Exception("Invalid Markdown, formatted section not closed.")
				
				processed_words.append(word.lstrip(delimiter).rstrip(delimiter))
			# else:
			# 	processed_words.append(word)

		processed_string = " ".join(processed_words)
		if has_end_space:
			processed_string += " "

		new_nodes.append(processed_string)

	final_nodes = []
	for new_node in new_nodes:
		# print(f" --NEW NODE-- {new_node}")
		final_nodes.append(TextNode(new_node, text_type))
	
	return final_nodes

