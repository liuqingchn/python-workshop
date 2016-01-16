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

	def ids(self):
		t = []
		for i in self.root.findall('./PubmedArticle/MedlineCitation/PMID'):
			t.append(i.text)
		return t

	def titles(self):
		t = []
		for i in self.articles:
			t.append(i.find('./ArticleTitle').text)
		return t

	def abstracts(self):
		t = []
		for i in self.articles:
			a = i.findall('./Abstract/AbstractText')
			b = '\n'.join([ j.text for j in a ])
			t.append(b)
		return t

	def journals(self):
		t = []
		for i in self.articles:
			t.append(i.find('./Journal/Title').text)
		return t

	# homework
	def authors(self):
		return []

	def date(self):
		return []




