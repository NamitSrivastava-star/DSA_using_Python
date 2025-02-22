class A(object):
    def __new__(cls):
         print(cls)
         print("Creating instance")
         print(id(super().__new__(cls)))
         print(super().__new__(cls))
         print(super())
         print(super())
         return super(A, cls).__new__(cls)

    def __init__(self):
        print("Init is called")
        print(self)
        print(id(self))