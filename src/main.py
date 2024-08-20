from textnode import TextNode
from htmlnode import HTMLNode
from markdown_to_html import *

import os
import shutil
import regex


DEBUG_PRINT = False
PUBLIC_PATH = os.path.abspath(os.path.join(os.curdir, 'public'))
STATIC_PATH = os.path.abspath(os.path.join(os.curdir, 'static'))
CONTENT_PATH = os.path.abspath(os.path.join(os.curdir, 'content'))
TEMPLATE_PATH = os.path.abspath(os.path.join(os.curdir, 'template.html'))


def main():

	# deletes public folder and copies static content
	clean_copy(STATIC_PATH, PUBLIC_PATH)

	# generate page and write to public folder
	generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, PUBLIC_PATH)


def extract_title(markdown: str):
	# pull the '# ' line from the page and return only the raw text
	lines = markdown.splitlines()
	for line in lines:
		if line[:2] == '# ':
			raw_line = line[2:]
			if DEBUG_PRINT:
				print("Heading found:", raw_line)
			return raw_line
	raise Exception("Header title not found")

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
	print(f'Generating page from \'{dir_path_content}\' to \'{dest_dir_path}\' using the template \'{template_path}\'\n')

	if not os.path.isdir(dir_path_content):
		raise Exception("Content directory cannot be found.")
	
	if not os.path.isfile(template_path):
		raise Exception("Template file cannot be found")

	if not os.path.isdir(dest_dir_path):
		raise Exception("Destination directory cannot be found")

	dir_contents = os.listdir(dir_path_content)
	for dir_item in dir_contents:
		abs_dir_item_path = os.path.join(dir_path_content, dir_item)
		if os.path.isdir(abs_dir_item_path):
			# content_path = os.path.join(dir_path_content, dir_item)
			dest_path = os.path.join(dest_dir_path, dir_item)

			os.mkdir(dest_path)
			print(f'Made new folder \n %%% {dest_path}')
			generate_pages_recursive(abs_dir_item_path, template_path, dest_path)

		elif os.path.isfile(abs_dir_item_path):
			# raw_markdown_path = os.path.join(dir_path_content, dir_item)
			raw_markdown_file = open(abs_dir_item_path, 'r')
			raw_markdown = raw_markdown_file.read()
			raw_markdown_file.close()

			original_template_file = open(template_path, 'r')
			original_template = original_template_file.read()
			original_template_file.close()

			user_html_content = markdown_to_html_node(raw_markdown).to_html()
			content_title = extract_title(raw_markdown)
			print(f'Generated page for {content_title}')

			html_content = original_template.replace("{{ Title }}", content_title)
			html_content = html_content.replace("{{ Content }}", user_html_content)

			new_file_name = dir_item.replace('.md', '.html')
			new_file_path = os.path.join(dest_dir_path, new_file_name)
			new_file = open(new_file_path, 'w')
			new_file.write(html_content)
			new_file.close()

	print("Generation of static site is complete.\n")


def generate_page(from_path: str, template_path: str, dest_path: str):
	print(f'Generating page from {from_path} to {dest_path} using {template_path}')

	if not os.path.isdir(from_path):
		raise Exception("Content directory cannot be found.")
	
	if not os.path.isfile(template_path):
		raise Exception("Template file cannot be found")

	if not os.path.isdir(dest_path):
		raise Exception("Destination directory cannot be found")
	
	raw_markdown_file = open(from_path, 'r')
	raw_markdown = raw_markdown_file.read()
	raw_markdown_file.close()

	original_template_file = open(template_path, 'r')
	original_template = original_template_file.read()
	original_template_file.close()

	user_html_content = markdown_to_html_node(raw_markdown).to_html()
	content_title = extract_title(raw_markdown)

	html_content = original_template.replace("{{ Title }}", content_title)
	html_content = html_content.replace("{{ Content }}", user_html_content)

	if not os.path.exists(os.path.dirname(dest_path)):
		print("Creating destination directory")
		os.mkdir(dest_path)
	
	file_name = os.path.basename(from_path)
	file_name = file_name.replace(".md", ".html")
	destination_file_path = os.path.join(dest_path, file_name)
	destination_file = open(destination_file_path, 'w')
	destination_file.write(html_content)
	destination_file.close()


####################################################

def clean_copy(src_dir: str, dst_dir: str):
	delete_directory(dst_dir)
	recursive_copy(src_dir, dst_dir)

def delete_directory(dir_path: str):
	if not os.path.exists(dir_path):
		print("Error path does not exist!")
		if DEBUG_PRINT:
			print(f'Failed to clean % {dir_path}')
		return
	
	shutil.rmtree(dir_path)
	print(f'Deleted the path % {dir_path}')

def recursive_copy(src_dir: str, dst_dir: str):
	if not os.path.exists(dst_dir):
		os.mkdir(dst_dir)
		print(f'Created directory % {dst_dir}')

	dir_ls = os.listdir(src_dir)
	for item in dir_ls:
		item_path = os.path.join(src_dir, item)
		if os.path.isdir(item_path):
			new_src_dir = os.path.join(src_dir, item)
			new_dst_dir = os.path.join(dst_dir, item)
			recursive_copy(new_src_dir, new_dst_dir)
		elif os.path.isfile(item_path):
			src_file = os.path.join(src_dir, item)
			dst_file = os.path.join(dst_dir, item)
			print(f'Copying file % {src_file} to {dst_file}')
			shutil.copy(src_file, dst_file)

if __name__ == "__main__":
	main()

