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
	root = etree.fromstring(response.text)
	ids = [ id.text for id in root.findall('./IdList/Id') ]

	EntrezFetchParams['id'] = ','.join(ids)
	response = requests.get(EntrezFetch, params=EntrezFetchParams)
	root = etree.fromstring(response.text)
	return Pubmed(root)

class Pubmed:
	def __init__(self, r):
		self.root = r
		self.articles = r.findall('./PubmedArticle/MedlineCitation/Article')

	def titles(self):
		t = []
		for i in self.articles:
			t.append(i.find('./ArticleTitle').text)
		return t



