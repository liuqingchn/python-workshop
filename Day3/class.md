
## Basic Object-oriented concepts

```
class Vector:
   counter = 0
   def __init__(self, u,v):
      self.u = u
      self.v = v
      Vector.counter += 1

```

Concepts:

- Class definition
- Object creation
- Special methods
- Object attributes versus class attributes

Exercises:

- Define the "norm" of a vector.

## Error handling

```
raise Exception("This is an error.")
```