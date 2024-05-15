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
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: str):
	if len(old_nodes) == 0:
		return []
	
	if delimiter == None or text_type == text_type_text:
		return old_nodes

	new_nodes = []
	for old_node in old_nodes:
		# print(f" --OLD_NODE-- {old_node}")
		processed_words = []

		# If its not a TextNode, then add, as is.
		if type(old_node) is not TextNode:
			# print(f" --NOT TEXTNODE-- {old_node}")
			new_nodes.append(old_node)

		words = old_node.text.split()
		for word in words:
			# print(f" --WORD-- \"{word}\"")
			# print(f" --DELIMITER-- \"{delimiter}\"")

			if delimiter in word:
				# Ensuring the delmiter closes
				begin_delimit_found: bool = word[:2] == delimiter
				end_delimit_found: bool = word[-2:] == delimiter
				if not ( begin_delimit_found and end_delimit_found ):
					print(f" --DELIMIT TEST-- {begin_delimit_found}, {end_delimit_found} in {word}")
					raise Exception("Invalid Markdown, formatted section not closed.")
				
				# print(f" --WORD-BF-PROC_WORDS-- \"{word}\"")
				if len(processed_words) != 0:
					# print(f" --PROC_WORDS-- {processed_words}")
					processed_string = " ".join(processed_words)
					new_nodes.append(TextNode(processed_string + " ", text_type_text))
					processed_words = []
				
				# print(f" --WORD-BF-PROC_WORDS-- \"{word}\" in \"{processed_words}\"")
				processed_words.append(word.lstrip(delimiter).rstrip(delimiter))
				processed_string = " ".join(processed_words)
				new_nodes.append(TextNode(processed_string, text_type))
				processed_words = []
				
			else:
				processed_words.append(word)
	
	processed_string = " ".join(processed_words)
	new_nodes.append(TextNode(" " + processed_string, text_type_text))
	
	# print(f" --final_nodes-- {new_nodes}")
	return new_nodes

# similar to split_nodes_delimiter - except always will operate on image types
def split_nodes_images(old_nodes):
	if len(old_nodes) == 0:
		return []
	
	img_node_list = list(map(lambda node: extract_markdown_image(node.text), old_nodes))[0]

	final_nodes = []
	split_list = []
	prev_delimit = ""

	for node in img_node_list:
		delimit = f"![{node[0]}]({node[1]})"
		split_list = list(map(lambda node_text: node_text.text.split(delimit, 2), old_nodes))[0]
		additional_img_list = extract_markdown_image(split_list[0])

		if not len(additional_img_list) == 0:
			additional_img_text = additional_img_list[0][0]

		if len(additional_img_list) == 0:
			final_nodes.append(TextNode(split_list[0], text_type_text))

		elif additional_img_text in split_list[0]:   
			sub_img_list = list(map(lambda text: text.split(prev_delimit, 2), [split_list[0]]))[0]
			middle_text = sub_img_list[-1]
			if not middle_text == "":
				final_nodes.append(TextNode(middle_text, text_type_text))

		prev_delimit = delimit
		final_nodes.append(TextNode(node[0], text_type_image, node[1]))

	if len(split_list[1]) != 0:
		# print(f" --END OF LINE-- {split_list[1]}")
		final_nodes.append(TextNode(split_list[1], text_type_text))

	# print(f" --FINAL-- {final_nodes}")
	return final_nodes

# similar to split_nodes_delimiter - except always will operate on link types
def split_nodes_link(old_nodes):
	# old_text_list = []
	if len(old_nodes) == 0:
		return []
	
	# for old_node in old_nodes:
	# 	old_text_list.append(old_node.text)

	url_list = list(map(lambda node: extract_markdown_url(node.text), old_nodes))[0]

	final_nodes = []
	text_list = []
	prev_delimit = ""

	for item in url_list:
		delimit = f"[{item[0]}]({item[1]})"

		text_list = list(map(lambda node_text: node_text.text.split(delimit, 2), old_nodes))[0]

		additional_link = extract_markdown_url(text_list[0])

		if not len(additional_link) == 0:
			additional_link_text = additional_link[0][0]

		if len(additional_link) == 0:
			final_nodes.append(TextNode(text_list[0], text_type_text))

		elif additional_link_text in text_list[0]:
			sub_text_list = list(map(lambda text: text.split(prev_delimit, 2), [text_list[0]]))[0]
			middle_text = sub_text_list[-1]
			if middle_text != "":
				final_nodes.append(TextNode(middle_text, text_type_text))

		prev_delimit = delimit
		final_nodes.append(TextNode(item[0], text_type_link, item[1]))

	if len(text_list[1]) != 0:
		final_nodes.append(TextNode(text_list[1], text_type_text))

	return final_nodes
	
def text_to_textnodes(text: str) -> list[TextNode]:

	list_parts = text.split(" ")
	print(list_parts)
	
	final_parts = []
	for part in list_parts:
		final_parts.append(split_nodes_delimiter([TextNode(part, text_type_text)], "**", "bold"))
 
	return final_parts
	