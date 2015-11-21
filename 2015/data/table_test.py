import table

t = table.read("iris.csv", "nnnnc")
t.cluster(['Petal.Width', 'Petal.Length'])
t.cluster(['Petal.Width', 'Petal.Length'], clusters=3)
t.cluster(['Petal.Width', 'Petal.Length'], method='hierarchical', clusters=3)
for r in t:
   print(r['_meanshift_'],r['_kmeans_'],r['_hierarchical_'],r['Species'],sep='\t')