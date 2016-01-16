import pubmed

res = pubmed.Search('breast cancer',10)
# print(res.titles())
# print(res.journals())
print(res.ids())
abstracts = res.abstracts()
print(abstracts[0])
