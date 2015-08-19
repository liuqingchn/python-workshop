from Bio import Entrez
from Bio import SeqIO

Entrez.email = "vinhthuyphan@gmail.com"

search_result = Entrez.esearch(db="nucleotide", term="brca1", retmax=20)
search_record = Entrez.read(search_result)

fetch_result = Entrez.efetch(db="nucleotide", id=search_record['IdList'], rettype="gb", retmode="text")
fetch_record = SeqIO.parse(fetch_result, "gb")