import sys

num_list = []
for num in range(100):
    print(num,sys.getsizeof(num_list),sep='-->')
    num_list.append(num)