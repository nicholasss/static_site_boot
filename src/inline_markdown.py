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
	pass

# similar to split_nodes_delimiter - except always will operate on link types
def split_nodes_link(old_nodes):
	old_text_list = []
	if len(old_nodes) == 0:
		return []
	
	for old_node in old_nodes:
		old_text_list.append(old_node.text)

		# if old_node.type != text_type_text:
		# 	raise ValueError(f"This function requires text_type of text - received {old_node.type}")

	# print(f" --OLD_TEXT_LIST-- {old_text_list}")

	# TODO is this array_0 at the end needed?
	url_list = list(map(lambda x: extract_markdown_url(x), old_text_list))[0]
	# print(new_nodes)

	# print(f" --NEW_NODES-- {new_nodes}")

	final_nodes = []
	text_list = []
	for item in url_list:
		delimit = f"[{item[0]}]({item[1]})"
		print(f" --DELIMIT-- {delimit}")
		text_list = list(map(lambda x: x.split(delimit, 1), old_text_list))[0]
		print(text_list)

		# TODO if switch for there is text between the links

		found_other_link = extract_markdown_url(text_list[0])
		if len(found_other_link) == 0:
			final_nodes.append(TextNode(text_list[0], text_type_text))
		elif found_other_link[0][1] in text_list[0]:
			print("other text between links likely - not added yet")
			# split and find end text of first item in text_list
		
		final_nodes.append(TextNode(item[0], text_type_link, item[1]))

	if len(text_list[1]) != 0:
		final_nodes.append(TextNode(text_list[1], text_type_text))


		# TODO what about the stuff between the links?

	# TODO return the list if there are no links

	return final_nodes
	