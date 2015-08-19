
Create a module that faciliates the analysis of column-formatted or tabular data.

```
import tabular

data = tabular.read("iris.csv", sep=",")
```

A list representing column "Species".
```
data['Species']
```

- data has N rows.
- each row is a dictionary; keys are from the header and values are from the row.