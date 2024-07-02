# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

nums = [3,2,2,3]
val = 3

output = []

#iterating through nums
for i in nums:
    #if element matches value
    if i == val:
        #we dont add it and just continue
        continue
    else:
        #if not we add it to output
        output.append(i)

print(output)