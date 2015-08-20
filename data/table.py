
class Table:
   def __init__(self, header, rows, types):
      if types is not None:
         self.types = [float if t=='n' else str for t in types]
      else:
         self.types = [str] * len(header)

      self.rows = [ self.make_row(header,row) for row in rows ]
      self.columns = {}

   def make_row(self, h, r):
      return { h[i] : self.types[i](r[i]) for i in range(len(r)) }

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

   def save(self):
      pass

## Input: a file and separator string
## Output: a Table object
## TODO: deal with '\t'.  How?
def read(input_file, types=None):
   rows = []
   header = ""
   f = open(input_file, "Ur")
   for line in f:
      if line.strip() != '':
         rows.append(line.strip().split(','))
   f.close()
   header = rows.pop(0)
   return Table(header, rows, types)
