# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3

nums = [3,6,9,1]

#we sort this 
nums.sort()

print(nums)
#initialize an empty array 
output = []

#iterating through teh length until the last but one index
for i in range(len(nums)-1):
    #we append the difference of elements i and i+1    
    output.append(nums[i+1]-nums[i])

print(max(output))