# 1. Import it
import argparse

# 2. Create a parser
parser = argparse.ArgumentParser()

# 3. Add argument(s)
parser.add_argument("square", help="display a square of a given number")

# 4. Parse argument(s)
args = parser.parse_args()

# 5. Access argument(s)
print(args.square * args.square)