# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

nums = [4,5,6,7,0,1,2]
target = 0

output = []

#iterating through indices of nums
for i in range(len(nums)):
    #if i finds a number equal to target
    if nums[i] == target:
        #add it to output
        output.append(i)


print(output)