
## Biopython

- Search and install biopython module using conda
- Documentation: read the source (http://biopython.org/DIST/docs/api/)

## Search and download articles

(1) Search, (2) Fetch, (3) Parse

- Bio.Entrez: esearch, efetch
- Bio.Medline: parse

```
from Bio import Entrez
handle = Entrez.esearch(db="pubmed", term="brca1", retmax=100)
record = Entrez.read(handle)
idlist = record["IdList"]


from Bio import Medline
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)
```

- investigate "records".  How?
