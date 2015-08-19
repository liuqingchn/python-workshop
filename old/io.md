
## Preliminaries

- Must have installed Python 3 Anaconda
- Editor: use your favorite or Sublime Text 3

## Print and format column-wise texts

Goals:

- Printing with the print() function.
- Review of loops and iterations.
- Generate well-formated texts and save them to files.

Code template:

```
for x in range(15):
   print(repr(x).rjust(2), repr(x*x).rjust(3))
```

Tasks:

- Add header.
- Add one more column (x^3) formatted to 4 spaces, right justified.

## Reading from files

```
f = open('workfile', 'r')
```

Understand:

- Error codes
- the dir() function
- f.read()
- f.readline()
- iterate a file each line at a time.

## Writing to files
```
f = open('workfile', 'w')
```

Understand:

- f.write()
- the type() function
- Other methods of TextIOWrapper; https://docs.python.org/3/
- What is the closed attribute?

Must close files after reading or writing!

Short cut:
```
with open('workfile', 'r') as f:
   data = f.read()
```

## File processing

- Process a file one line at a time.
- String splitting.
- List


Exercises:

- Given a FASTA file, return the DNA sequence(s) in the file.
- Given a column-formated file, create a dictionary called Column with keys from the header and values from the rows.   Example: Column['Species'] corresponds to the column with Species.
- Given a column-formated file with N rows (not counting the header), create a list called Rows of N dictionaries.  Rows[0] is a dictionary with keys from the header and values from the first row.   Example: Rows[0]['Species'] corresponds to the first value in column Species.


