# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter

nums = [-1,0,1,2,-1,-4]

#initialize an empty array for storing the values
output = []

#go through the first index first
for i in range(len(nums)):
    #iterate through second index to end
    for j in range(i+1,len(nums)):
        #iterate through third index to end
        for k in range(j+1,len(nums)):
            #now, we add the values at these indexes and see if it matches 0
            if nums[i] + nums[j] + nums[k] == 0:
                #add them to output
                output.append([nums[i],nums[j],nums[k]])



print((output))





























