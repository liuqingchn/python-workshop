
Create a module that faciliates the analysis of column-formatted or tabular data.

```
import tabular

f = tabular.read("iris.csv", sep=",")
print(f['Species'])
```

f['Species'] is a list representing column "Species".