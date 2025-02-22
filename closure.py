def func1(num):
    def func2(x):
        return x ** num
    return func2

result = func1(2)   
print(result(3))     