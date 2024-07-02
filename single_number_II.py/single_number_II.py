# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99


nums = [0,1,0,1,0,1,99]

for i in nums:
    if nums.count(i) == 1:
        print(i)