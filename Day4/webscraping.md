
Goal: download descriptions of genes that are related to a particular key.

## Regular expression

```
import re
re.match("/gene/\d+", "/gene/20")
```

Regular expression syntax: https://docs.python.org/3/library/re.html#regular-expression-examples


## Web scapping

```
import requests
from bs4 import BeautifulSoup

s = requests.Session()
ncbi_result = s.get("http://www.ncbi.nlm.nih.gov/gene/?term=brca1")

soup = BeautifulSoup(ncbi_result.content)
soup.find_all('a')
genes = [ a for a in soup.find_all('a') if re.match("/gene/\d+", a['href']) ]

gene_urls = [ 'http://www.ncbi.nlm.nih.gov' + a['href'] for a in genes ]

gene_result = s.get(gene_urls[0])
gene_soup = BeautifulSoup(gene_result.content)
gene_soup.find_all("dl", id="summaryDl")
```


Key things:

- requests_result = requests.get(url) or  
- session = requests.Session(); requests_result = session.get(url)


- soup = BeautifulSoup(requests_result.content)
- soup.find_all(tag)
- soup.find_all(tag, id=something)
- soup.find_all(tag, class_=something)

- list comprehension
- matching with regular expression: re.match(pattern, string)

Learn to find and read online documentations!!!