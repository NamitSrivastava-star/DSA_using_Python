import time

def timer(delay):
    def timer_function(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            time.sleep(delay)
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Execution time taken of a function name is {func.__name__} is {end-start}")
            return result
        return wrapper
    return timer_function

@timer(10)
def display():
    print("Hello")

if __name__ == '__main__':
    display()