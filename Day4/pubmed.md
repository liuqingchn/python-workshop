
## Biopython

- Search and install biopython module using conda
- Documentation: read the source (http://biopython.org/DIST/docs/api/)

## Search and download articles

(1) Search, (2) Fetch, (3) Parse

- Bio.Entrez: esearch, efetch
- Bio.Medline: parse

```
from Bio import Entrez, Medline

Entrez.email = "A.N.Other@example.com"
search_handle = Entrez.esearch(db="pubmed", term="breast+cancer", retmax=10)
search_result = Entrez.read(search_handle)

fetch_handle = Entrez.efetch(db="pubmed", id=search_result['IdList'], rettype="medline", retmode="text")
records = Medline.parse(fetch_handle)
```

- investigate "records".  How?
