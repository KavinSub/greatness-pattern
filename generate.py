# Author: Kavin Subramanyam

# Third party libraries
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
	
	# Now retrieve all successors from the list
	successors_list_items = parser.findAll('li')
	successors = [str(successor.getText()) for successor in successors_list_items]
	return successors
		
if __name__ == '__main__':
	document = download_person("Isaac Newton")
	successors = retrieve_successors(document, physicist_tags)