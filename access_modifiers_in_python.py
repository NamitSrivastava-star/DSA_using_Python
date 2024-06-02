"""
Access Modifiers in Python
"""

class Access:
    def __init__(self, public_value, protected_value, private_value):
        self.public = public_value
        self._protected = protected_value
        self.__private = private_value


if __name__ == '__main__':
    access_obj = Access(10,80,20)
    print("Public Access value", access_obj.public)
    print("Protected Access value", access_obj._protected)
    # print("Private Access value", access_obj.__private)        
    print("Private Access value using name Mangling", access_obj._Access__private)