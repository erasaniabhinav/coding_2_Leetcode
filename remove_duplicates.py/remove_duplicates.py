# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

nums = [0,0,1,1,1,2,2,3,3,4]

#initialize an empty array
output = []

#iterating through nums
for i in nums:
    #if i not in output then we add it to output
    if i not in output:
        output.append(i)

print(output)