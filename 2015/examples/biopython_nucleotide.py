from Bio import Entrez, SeqIO

Entrez.email = "vinhthuyphan@gmail.com"

## search, fetch nucleotide database from Entrez
search_result = Entrez.esearch(db="nucleotide", term="brca1", retmax=20)
search_record = Entrez.read(search_result)
fetch_result = Entrez.efetch(db="nucleotide", id=search_record['IdList'], rettype="gb", retmode="text")

## parse nucleotide from result
fetch_record = SeqIO.parse(fetch_result, "gb")