def print_subsets(index, nums, visited):
        if index == len(nums):
            print(visited)
            return

        visited.append(nums[index])
        print_subsets(index + 1, nums, visited)
        visited.pop()
        print_subsets(index + 1, nums, visited)

print_subsets(0, [1, 2, 3], [])        