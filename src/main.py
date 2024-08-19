from textnode import TextNode
from htmlnode import HTMLNode

import os
import shutil


DEBUG_PRINT = True
PUBLIC_PATH = os.path.abspath(os.path.join(os.curdir, 'public'))
STATIC_PATH = os.path.abspath(os.path.join(os.curdir, 'static'))


def main():
	clean_copy(STATIC_PATH, PUBLIC_PATH)


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

