def types_converter(types):
   if types is None:
      return None
   return [ float if t=='n' else str for t in types ]

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--types")
args = parser.parse_args()

converter = types_converter(args.types)
rows = []
header = ""
i = 0
f = open(args.input_file, "Ur")
for line in f:
   if line.strip() != '':
      row = line.strip().split(',')
      if i>0 and converter is not None:
         row = [ converter[i](row[i]) for i in range(len(row)) ]
      rows.append(row)
      i = i+1
f.close()
print(rows)
