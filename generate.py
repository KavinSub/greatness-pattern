# Author: Kavin Subramanyam

# Built-in modules
from collections import deque, defaultdict
import re
import unicodedata

# Third party modules
from BeautifulSoup import BeautifulSoup

# Personal modules
from download import download_person

physicist_tags = ["notable students", "doctoral students"]

# Args:
#	document - the html document of a person
# Retrieve the successors of an individual
def retrieve_successors(document, acceptable_tags):
	# Retrieve the infobox table
	parser = BeautifulSoup(document)
	content = str(parser.find('table', {'class':'infobox vcard'}))
	if content is None:
		return []
	# Retrieve the correct table row (<tr>)
	parser = BeautifulSoup(content)
	table_rows = parser.findAll('tr')
	correct_row = ''
	for row in table_rows:
		parser = BeautifulSoup(str(row))
		header = parser.findChild('th')
		if header is None:
			continue
		header_text = header.getText().lower()
		if header_text in acceptable_tags:
			correct_row = row
			break
	
	if correct_row is None:
		return []

	# Now retrieve all successors from the list
	parser = BeautifulSoup(str(correct_row))
	successors_list_items = parser.findAll('a', {'title': re.compile('.+')})
	successors = [unicodedata.normalize('NFKD', successor.getText()).encode('ascii', 'ignore') for successor in successors_list_items]
	print(successors)
	return successors

# Args: None
# Basic test to ensure retrieve_successors is working as intended.
def simple_test():
	document = download_person("Isaac Newton")
	successors = retrieve_successors(document, physicist_tags)
	print(successors)

		
if __name__ == '__main__':

	root = "Max Planck"

	physicists = {}

	queue = deque()
	queue.append(root)

	while len(queue) > 0:
		physicist = queue.popleft()
		
		document = download_person(physicist)
		successors = retrieve_successors(document, physicist_tags)

		physicists[physicist] = []
		for successor in successors:
			physicists[physicist].append(successor)
			queue.append(successor)

	print(physicists)