## test.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()

rows = []
f = open(args.input_file, "Ur")
for line in f:
   rows.append( line.strip().split(',') )
f.close()
print(rows)

