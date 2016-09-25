# Author: Kavin Subramanyam
# This module contains functions to download html content.

# Third party libraries
import requests

# Args:
# 	name - Name of the individual. 
# Retrieves the html content of the person from the relevant wikipedia page.
def download_person(name):
	response = requests.get('https://en.wikipedia.org/wiki/{}'.format(name))
	return response.text

if __name__ == '__main__':
	pass