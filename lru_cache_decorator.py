from time import time
from functools import lru_cache

@lru_cache(maxsize = 10000)
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n >= 2:
        return fib(n - 1) + fib(n - 2)
    
if __name__ == '__main__':
    start = time()
    for i in range(30):
        print(fib(i))

    end = time()
    print("Time Taken: ", end - start)    
