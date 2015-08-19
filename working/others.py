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

import math

class Vector:
   def __init__(self, a, b):
      print("i am in __init__")
      self.x = a
      self.y = b

   def norm(self):
      return math.sqrt(self.x*self.x + self.y*self.y)

   def add(self, c):
      return self.x + self.y + c

my_vector = Vector(3,4)
print(my_vector.norm())
print(my_vector.add(5))