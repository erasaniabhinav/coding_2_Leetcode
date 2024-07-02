# Input: nums = [1,3,5,6], target = 5
# Output: 2


nums = [1,3,5,6]
target = 5

#iterates through nums linearly in O(n) time complexity
for i in range(len(nums)):
    #if value at index matches target
    if nums[i]==target:
        print(i)