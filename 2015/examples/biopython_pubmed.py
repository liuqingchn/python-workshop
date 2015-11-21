from Bio import Entrez, Medline

Entrez.email = "vinhthuyphan@gmail.com"

## search, fetch pubmed database from Entrez
search_result = Entrez.esearch(db="pubmed", term="breast+cancer", retmax=10)
search_record = Entrez.read(search_result)
fetch_result = Entrez.efetch(db="pubmed", id=search_record['IdList'], rettype="medline", retmode="text")

## parse abstract from result
fetch_record = Medline.parse(fetch_result)

