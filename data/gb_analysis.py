
def process(line):
   tmp = line.strip().strip('gene ').strip('complement(').strip(')')
   start, end = tmp.split('..')
   return ('complement' not in line, int(start), int(end))

def gene_lengths(genes):
   lengths = [ g[2]-g[1]+1 for g in genes ]
   return lengths


f = open("deinococcus.gb", "Ur")
genes = [ process(line) for line in f if line.strip().startswith('gene') ]
on_complement = [ g for g in genes if g[0]==False ]
f.close()
print("There are", len(genes), "genes")
print(gene_lengths(genes))
print("There are ", len(on_complement), "genes on the complement", on_complement)