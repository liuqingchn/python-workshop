import table

h = ['name', 'age', 'salary']
rows = [['john',23,56000], ['mary',19,25000],['steve',50,150000]]

t = table.Table(h,rows)
print("Column name:", t['name'])
print("Going through all rows")
for row in t:
   print(row)
print("All rows", [row for row in t])
print("All rows with salary > 30,000:",  [ row for row in t if row['salary'] > 30000])
print("Name of people with salary > 30,000:", [ row['name'] for row in t if row['salary']>30000])