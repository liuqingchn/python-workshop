import re
import requests
from bs4 import BeautifulSoup

s = requests.Session()
ncbi_result = s.get("http://www.ncbi.nlm.nih.gov/gene/?term=breast+cancer")

soup = BeautifulSoup(ncbi_result.content)
soup.find_all('a')
genes = [ a for a in soup.find_all('a') if re.match("/gene/\d+", a['href']) ]

gene_urls = [ 'http://www.ncbi.nlm.nih.gov' + a['href'] for a in genes ]

gene_result = s.get(gene_urls[0])
gene_soup = BeautifulSoup(gene_result.content)
results = gene_soup.find_all("dl", id="summaryDl")

results[0].prettify()
results[0].text