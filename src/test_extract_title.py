import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
	def test_extract_title(self):
		title_md_one = "# Heading one"
		title_extracted = "Heading one"
		self.assertEqual(extract_title(title_md_one), title_extracted)

	