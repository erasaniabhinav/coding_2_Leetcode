# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

# for elements in range of nums
for i in range(len(nums)):
    # elements in range next to i 
    for j in range(i+1,len(nums)):
        #if elements sum matches target
        if nums[i]+nums[j] == target:
            #we print the indexes
            print(i,j)



