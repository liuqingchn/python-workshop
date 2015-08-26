import table

t = table.read("iris.csv", "nnnnc")
t.kmeans(["Sepal.Width", "Sepal.Length", "Petal.Width", "Petal.Length"], k=3)
result = [ (r['KMEANS'], r['Species']) for r in t]
for r in result:
	print(r[0],"\t", r[1])
