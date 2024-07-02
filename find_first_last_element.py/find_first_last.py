# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

nums = [5,7,7,8,8,10]
target = 8

output = []

#iterating through len of nums
for i in range(len(nums)):
    #if value at index equals target
    if nums[i] == target:
        #add to output
        output.append(i)


#print it
print(output)