class Vector:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def __init__(self):
    return 'Vector (%d,%d)' % (self.a,self.b)

  def __add__(self,other):
    return Vector(self.a + other.a, self.b+other.b)

v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1+v2)
