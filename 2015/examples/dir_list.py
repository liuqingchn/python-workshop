import argparse
from os import listdir, path
from os.path import isfile, join

parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

onlyfiles = [ f for f in listdir(args.dir) if path.isfile(path.join(args.dir,f)) ]
print(onlyfiles)