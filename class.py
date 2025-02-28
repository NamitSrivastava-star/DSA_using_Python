n = 5
d = { 'x' : 1, 'y' : 2 }

class Foo:
    pass

x = Foo()

for obj in (n, d, x):
    print(obj)
    print(obj.__class__)
    print(type(obj))
    print(type(obj) is obj.__class__)


tuple1 = (1,)
print(type(tuple1))

for val in tuple1:
    print(val)

class A:
    def __init__(self, data):
        self.data = data    

    def __add__(self, b): # operator overloading in python
        return self.data + b.data
    
class B:
    def __init__(self, data):
        self.data = data   

a = A(10)
b = B(20)
print(a + b)  # add to objects               