# Ch 4 Part 3: Block to HTML

# Take a given block of markdown and convert it to an HTML Node

from block_markdown import *
from htmlnode import *


# ================================
# Block Types to HTML Node
# ================================

# Paragraph

# Heading - '# ' --> '###### '

# Code - ' ```code``` `

# Quote - '> quote' on multiple lines

# Unordered List - '- ' or '* ' on multiple lines

# Ordered List - '1. ' on multiple lines (ascending)

# ================================
# Conversion Function
# ================================

def markdown_to_html_node(markdown: str):
	# Ensure to include top level <div></div>
	pass

