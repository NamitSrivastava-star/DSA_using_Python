"""
Rotate Array Brute Force Solution
"""

def rotate_array(nums: list, k:int)-> None:
    temp_nums = [0] * len(nums) #create an temporay array of same size as of nums
    for index, value in enumerate(nums):
        temp_nums[(index + k) % len(nums)] = value

    #Copy temp_nums array back to nums array because we need to do in-place rotation as mention in problem statement
    nums = temp_nums
    print(nums)    

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3     
    rotate_array(nums=nums, k=k)