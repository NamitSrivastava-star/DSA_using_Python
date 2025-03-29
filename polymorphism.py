
class Polymorphism:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum_with_zero_args(self):
        return self.x + self.y
    
    def sum_with_one_args(self, val):
        return 'Hello' + val
    
    def sum(self, x = None, y = None):
        if x is None and y is None:
           return self.sum_with_zero_args()
        elif y is None:
           return self.sum_with_one_args(x)
        else:
            return x + y
    


if __name__ == "__main__":
    poly_obj = Polymorphism(2,3)
    print("Sum with two args", poly_obj.sum(10,20))
    print("Sum with one args", poly_obj.sum("Ram"))
    print("Sum with zero args", poly_obj.sum())