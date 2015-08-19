f = open("workfile", "r")
data = f.read()
print(data)
f.close()

f = open("workfile", "r")
for line in f:
   print(line)
f.close()