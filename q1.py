def find_pair(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        num_dict[num] = i
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_dict and num_dict[diff] != i:
            return (num, diff)
    return "Pair not found
nums = [8, 7, 2, 5, 3, 1]
target = 10
print(find_pair(nums, target))  

nums = [5, 2, 6, 8, 1, 9]
target = 12
print(find_pair(nums, target)) 
