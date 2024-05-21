# Markdown Functions

from re import findall
from textnode import *

# '*' -> text_type_italic
def delimiter_to_text(delimiter: str) -> str:
	if "**" == delimiter:
		return text_type_bold
	elif "*" == delimiter:
		return text_type_italic
	elif "`" == delimiter:
		return text_type_code
	else:
		return text_type_text

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

		# If its not a TextNode, then add as is.
		if type(old_node) is not TextNode:
			# print(f" --NOT TEXTNODE-- {old_node}")
			new_nodes.append(old_node)
			continue

		if old_node.text_type != text_type and old_node.text_type != text_type_text:
			new_nodes.append(old_node)
			continue

		begin_delimiter_found = False
		end_delimiter_found = False
		in_delimiter_section = False

		words = old_node.text.split()
		for word in words:
			# print(f" --WORD-- \"{word}\"")
			# print(f" --DELIMITER-- \"{delimiter}\"")

			if delimiter in word:
				# print(f" --WORD-BF-PROC_WORDS-- \"{word}\"")
				if len(processed_words) != 0:
					# print(f" --PROC_WORDS-- {processed_words}")
					processed_string = " ".join(processed_words)
					new_nodes.append(TextNode(processed_string + " ", text_type_text))
					processed_words = []

				# Ensuring the delmiter closes
				begin_delimiter_found = delimiter in word[:2]
				end_delimiter_found = delimiter in  word[-2:]
				if not ( begin_delimiter_found and end_delimiter_found ):

					# index of current word in word list
					# if words after the current word have the end delimiter (end of string)
					# then set in_delimiter_section to true

					# TODO  multi-part i.e. **bolded word**
					print(f" --DELIMIT TEST-- {begin_delimiter_found}, {end_delimiter_found} in {word} with delimiter: {delimiter}")
					raise Exception("Invalid Markdown, formatted section not closed.")
				
				
				# print(f" --WORD-BF-PROC_WORDS-- \"{word}\" in \"{processed_words}\"")
				processed_words.append(word.lstrip(delimiter).rstrip(delimiter))
				processed_string = " ".join(processed_words)
				new_nodes.append(TextNode(processed_string, text_type))
				processed_words = []
				
			else:
				processed_words.append(word)

			# Clearing and appending buffers (processed_words/string)
			if words[-1] == word: # on last word of node
				processed_string = " ".join(processed_words)
				if old_nodes[-1] != old_node: # not on last node in list
					processed_string += " "
				if not processed_string == "":
					new_nodes.append(TextNode(" " + processed_string, text_type_text))
	
	# print(f" --final_nodes-- {new_nodes}")
	return new_nodes

# similar to split_nodes_delimiter - except always will operate on image types
def split_nodes_images(old_nodes):
	# print(f" --OLD_NODES-- {old_nodes}")

	if len(old_nodes) == 0:
		raise Exception("Empty list was provided")
	
	
	img_node_list = list(map(lambda node: extract_markdown_image(node.text), old_nodes))[0]

	if len(img_node_list) == 0:
		return old_nodes

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

	if len(old_nodes) == 1:
		# print(f" --END OF LINE-- {split_list}")
		return final_nodes

	if len(split_list[1]) != 0:
		# print(f" --END OF LINE-- {split_list[1]}")
		final_nodes.append(TextNode(split_list[1], text_type_text))

	# print(f" --FINAL-- {final_nodes}")
	return final_nodes

# similar to split_nodes_delimiter - except always will operate on link types
def split_nodes_link(old_nodes):
	# old_text_list = []

	# print(f" --OLD_NODES-- {old_nodes}")

	if len(old_nodes) == 0:
		raise Exception("Empty list was provided")

	url_list = list(map(lambda node: extract_markdown_url(node.text), old_nodes))[0]

	if len(url_list) == 0:
		return old_nodes

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

	print(text)

	raw_node = [TextNode(text, text_type_text)]

	# First look for link objects
	partial_proc_node = split_nodes_images(raw_node)
	partial_proc_node = split_nodes_link(partial_proc_node)

	# go through each option and pull out each
	for delimiter in textnode_delimiters:
		delimiter_text = delimiter_to_text(delimiter)
		partial_proc_node = split_nodes_delimiter(partial_proc_node, delimiter, delimiter_text)


	final_nodes = partial_proc_node
 
	return final_nodes
	