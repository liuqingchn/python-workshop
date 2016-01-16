import pubmed

res = pubmed.Search('breast cancer',10)
print(res.titles())