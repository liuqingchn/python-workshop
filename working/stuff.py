## stuff.py
def even(a):
   return [i for i in a if i%2==0]

def double(a):
   return [ i*2 for i in a ]

def not_divisible_by_5(a):
   return [ i for i in a if i%5 != 0 ]