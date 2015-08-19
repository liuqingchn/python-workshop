
## Search and download sequences

```
from Bio import Entrez
handle = Entrez.esearch(db="nucleotide", term="brca1", retmax=20)
record = Entrez.read(handle)

from Bio import SeqIO
handle = Entrez.efetch(db="nucleotide", id=record['IdList'], rettype="gb", retmode="text")
records = SeqIO.parse(handle, "gb")
```