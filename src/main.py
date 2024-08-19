from textnode import TextNode
from htmlnode import HTMLNode

import os
import shutil


DEBUG_PRINT = True
PUBLIC_PATH = os.path.abspath(os.path.join(os.curdir, 'public'))
STATIC_PATH = os.path.abspath(os.path.join(os.curdir, 'static'))


def main():
	clean_dir(PUBLIC_PATH)


# Recursive func to copy all contents from static to public dirs
def clean_dir(dir_path: str):
	if not os.path.exists(dir_path):
		print("Error path does not exist!")
		if DEBUG_PRINT:
			print(f'Failed to clean % {dir_path}')
	
	print("Are you sure you want the following dir deleted?")
	print(dir_path)
	answer = input("(y/n) % ")
	if answer == 'y':
		shutil.rmtree(dir_path)
		print(f'Cleaned the path % {dir_path}')
	else:
		print("Did not clean the path.")


if __name__ == "__main__":
	main()

