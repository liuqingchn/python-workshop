def double(a):
   # b = [i*2 for i in a]
   b = []
   for i in a:
      b.append(i*2)
   return b
def square(x):
   return x*x

def square_each(a):
   b = []
   for i in a:
      b.append(square(i))
   return b

### find indices of occurrences of x
def index(L, letter):
   idx = []
   for j in range(len(L)):
      # check if L[j] is equal to letter
      if L[j] == letter:
         idx.append(j)
   return idx

