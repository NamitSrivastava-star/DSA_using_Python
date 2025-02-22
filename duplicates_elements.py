from typing import List

def find_duplicate(lst: List)->None:
    num = set()
    for val in lst:
        if val in num:
            print(val)
        num.add(val)    


if __name__ == '__main__':
    my_list = [4,2,2,5,6,8,9,7,6,5,1,2,9]
    find_duplicate(my_list)