import re
import requests

session = requests.Session()
page = session.get("http://www.ncbi.nlm.nih.gov/pubmed/26276891")

## Non gredying matching
re.search("<AbstractText[\sa-zA-Z=\"]+>.+</AbstractText>", page.text)

## Get the text only
re.search("<AbstractText[\sa-zA-Z=\"]+>(.+)</AbstractText>", page.text)

## Greedy matching
re.search("<AbstractText[\sa-zA-Z=\"]+>.+?</AbstractText>", page.text)