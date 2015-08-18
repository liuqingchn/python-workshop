import math

class Vector:
   counter = 0
   def __init__(self, u,v):
      self.u = u
      self.v = v
      Vector.counter += 1

   def norm(self):
   	return math.sqrt(self.u*self.u + self.v*self.v)



x = Vector(3,4)
print(x.u, x.v)
print(x.norm())