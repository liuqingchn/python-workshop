#
# Find recent abstracts related to genes of interest on a topic
#
import re
import requests
from bs4 import BeautifulSoup

KEYWORDS = "breast+cancer"
GENES = ['BRCA1', 'BRCA2']

def search_pubmed(keywords):
   r = requests.get("http://www.ncbi.nlm.nih.gov/pubmed/?term="+keywords)
   soup = BeautifulSoup(r.text)
   PMID = soup.find_all("dl", class_="rprtid")
   return [ i.text.strip().strip('PMID: ') for i in PMID ]

def get_abstract(ids):
   pubmed_url = "http://www.ncbi.nlm.nih.gov/pubmed/"
   abstract = []
   for i in ids:
      article_url = pubmed_url + i
      article_page = requests.get(article_url)
      soup = BeautifulSoup(article_page.text)
      ab = soup.find_all("div", class_="abstr")
      abstract.append((i, ab[0]))
   return abstract

#
# select all abstracts a, for which there is a gene in "genes" that is
# in the abstract a.
#
def filter_abstracts(abstracts, genes):
   return [a for a in abstracts if len([g for g in genes if g in a[1]])>0 ]

ids = search_pubmed(KEYWORDS)
abstract = get_abstract(ids)
print(abstract[0])