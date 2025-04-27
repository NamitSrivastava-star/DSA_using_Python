from collections import defaultdict

def duplicate_elements(num, input1):

    if int(num) <= 0:
        return [-1]
    
    if len(input1) == 0:
        return [-1]
    
    if len(input1) != int(num):
        return [-1]
    
    nums = defaultdict(int)
    count = 0
    input2 = []
    for value in input1:
        if value not in nums:
            nums[value] = count + 1
        else:    
            nums[value] = nums[value] + 1

    for key, value in nums.items():
        if value > 1:
            input2.append(key)

    if len(input2) == 0:
        return [-1]

    return sorted(input2)                 


if __name__ == '__main__':
    num = 7
    input1 = []
    print(duplicate_elements(num, input1))
