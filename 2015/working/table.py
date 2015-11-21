
class Table:
   def __init__(self, header, rows):
      self.rows = [ dict(zip(header,r)) for r in rows ]
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


