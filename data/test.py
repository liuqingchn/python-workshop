# What is the state with highest murder rate in Blue states?
import table
data = table.read("crimeRatesByState2005.csv", "cnnnnnnnnc")
# m = max(row["murder"] for row in data if row['politics']=='Blue')
# s = [ (row["state"],row["murder"]) for row in data if row["murder"]==m and row['politics']=='Blue']


selected = [ row for row in data if row['politics']=='Blue']
max_row = selected[0]
for row in selected:
   if max_row['murder'] < row['murder']:
      max_row = row

print(max_row)
