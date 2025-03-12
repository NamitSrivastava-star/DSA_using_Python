def generate_numbers(num):
    for index in range(1, num):
        yield index

if __name__ == '__main__':
    generate_num = generate_numbers(5)
    print(next(generate_num))        
    print(next(generate_num))        
    print(next(generate_num))        
    print(next(generate_num))        
    print(next(generate_num))        