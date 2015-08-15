
class Table:
   def __init__(self, header, rows, types=None):
      if types is None:
         self.rows = [ dict(zip(header,row)) for row in rows ]
      else:
         self.rows = [ dict(zip(header, [types[i](r) for i,r in enumerate(row)])) for row in rows ]
      self.columns = {}

   ## get column by key
   def __getitem__(self, key):
      if key not in self.columns:
         self.columns[key] = [ r[key] for r in self.rows ]
      return self.columns[key]

   ## enumerate through self.rows
   def __iter__(self):
      self.i = -1
      return self

   def __next__(self):
      if self.i < len(self.rows)-1:
         self.i += 1
         return self.rows[self.i]
      else:
         raise StopIteration


## Input: a file and separator string
## Output: a Table object
def new_table(file, separator="\t"):
   pass

import csv
def read(filename, sep=',', types=None):
   ''' Default setting assumes the file is tab-delimited '''
   rows = []
   with open(filename, 'rU') as f:
      reader = csv.reader(f, delimiter=sep)
      for row in reader:
         rows.append(row)
   return Table(rows.pop(0), rows, types)


# t = read("iris.csv", types=[float,float,float,float,str])
# # t = read("crimeRatesByState2005.csv")
# print(t['Sepal.Length'])
