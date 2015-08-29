from sklearn.cluster import KMeans, DBSCAN, SpectralClustering, AgglomerativeClustering, MeanShift
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import kneighbors_graph

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

   def cluster(self, columns, **argv):
      option = {}
      Estimator = dict(kmeans=KMeans, meanshift=MeanShift, dbscan=DBSCAN, hierarchical=AgglomerativeClustering, spectral=SpectralClustering)

      if argv.get('method') is None:
         method = 'meanshift' if argv.get('clusters') is None else 'kmeans'
      else:
         if argv.get('method') not in Estimator:
            raise Exception("Unknown clustering method: " + argv.get('method'))
         method = argv.get('method', 'meanshift')

      if method == 'meanshift':
         pass
      elif method == 'dbscan':
         option['eps'] = argv.get('spacing', 0.3)
      else:
         if argv.get('clusters') is None:
            raise Exception("Must specify 'clusters', which is a number greater than 1.")
         option['n_clusters'] = argv.get('clusters')
         if argv.get('method') == 'hierarchical':
            option['linkage'] = argv.get('linkage', 'average')
            option['affinity'] = argv.get('affinity', 'euclidean')
         elif argv.get('method') == 'spectral':
            option['affinity'] = argv.get('affinity', 'rbf')

      est = Estimator.get(method)(**option)

      ## Select data
      rows = [ [r.get(c) for c in columns] for r in self.rows ]
      if argv.get('scaled') == True:
         rows = StandardScaler().fit_transform(rows)

      ## Cluster and store results
      labels = est.fit_predict(rows)

      print("\tClustering method: ", method, "\tNumber of clusters: ", len(set(labels)))

      for i in range(len(self.rows)):
         self.rows[i]['_' + method + '_'] = labels[i]

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
