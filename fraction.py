class Fraction:
    def __init__(self, num, den):
        self.__num = num   
        self.__den = den   

    def __str__(self):
        return f"{self.__num}/{self.__den}" 
    
    def addition(self, other):
        num = self.__num * other.__den + other.__num * self.__den
        den = self.__den * other.__den
        return str(num) + '/' + str(den)
    
    def subtraction(self, other):
        num = self.__num * other.__den - self.__den * other.__num
        den = self.__den * other.__den
        return str(num) + '/' + str(den)
    
    def multiplication(self, other):
        num = self.__num * other.__num
        den = self.__den * other.__den
        return str(num) + '/' + str(den)
    
    def division(self, other):
        num = self.__num * other.__den
        den = self.__den * other.__num
        return str(num) + '/' + str(den)



if __name__ == '__main__':
    fraction_obj1 = Fraction(7,9)
    fraction_obj2 = Fraction(1,2)
    print("Fraction Object1 ", fraction_obj1)
    print("Fraction Object2 ", fraction_obj2)
    print("Addition ", fraction_obj1.addition(fraction_obj2)) 
    print("Subtraction ", fraction_obj1.subtraction(fraction_obj2))   
    print("Multiplication ", fraction_obj1.multiplication(fraction_obj2))
    print("Division ", fraction_obj1.division(fraction_obj2))   