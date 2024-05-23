class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}" 


if __name__ == '__main__':
    fraction_obj = Fraction(7,9)
    print(fraction_obj)       