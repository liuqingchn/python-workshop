import requests
import xml.etree.ElementTree as etree

EntrezSearch = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
EntrezSearchParams = {'db':'pubmed'}
EntrezFetch = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
EntrezFetchParams = {'db':'pubmed', 'rettype':'xml'}


def Search(query, num_of_articles=5):
	EntrezSearchParams['retmax'] = num_of_articles
	EntrezSearchParams['term'] = query
	response = requests.get(EntrezSearch, params=EntrezSearchParams)
	root = etree.fromstring(response.content)
	ids = [ id.text for id in root.findall('./IdList/Id') ]

	EntrezFetchParams['id'] = ','.join(ids)
	response = requests.get(EntrezFetch, params=EntrezFetchParams)
	return etree.fromstring(response.content)

class Article(object):
	def __init__(self, articles=[]):
		self.articles = articles

	def keywords(self, k):
		pass


a = Search('breast cancer')
print(a[0].findall('./MedlineCitation'))