from sklearn.cluster import KMeans

class Table:
   def __init__(self, header, rows, types):
      if types is not None:
         self.types = [float if t=='n' else str for t in types]
      else:
         self.types = [str] * len(header)

      self.rows = [ self.make_row(header,row) for row in rows ]
      self.columns = {}
      self.keys = header

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

   def kmeans(self, columns, k=3):
   	rows = [ [r.get(c) for c in columns] for r in self.rows ]
   	est = KMeans(n_clusters=k)
   	results = est.fit_predict(rows)
   	for i in range(len(self.rows)):
   		self.rows[i]['KMEANS'] = results[i]

   def dbscan(self):
   	pass

   def svm(self):
   	pass

   def random_forrest(self):
   	pass
   	
   def save(self):
      pass


#############################################################
# Read comma-separated or tab-separated files.
# Return a table
#############################################################
def read(input_file, types=None):
   sep = ',' if input_file.endswith('.csv') else '\t'
   with open(input_file, "Ur") as f:
      rows = [ line.strip().split(sep) for line in f if line.strip() != '' ]
   header = rows.pop(0)
   return Table(header, rows, types)
