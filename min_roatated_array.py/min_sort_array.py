# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Input: nums = [4,5,6,7,0,1,2]


nums = [4,5,6,7,0,1,2]

l = 0
r = len(nums)-1

#output = []

# while l is less than r 
while l < r:
    if nums[l] < nums [r]:
        output = nums[l]
        break

    mid = (l+r)//2 
    
    #if nums of mid is less than l
    #we will search in the right side array
    if nums[mid] >= nums[l]:
        l = mid + 1
    #we will search for left side array
    else:
        r = mid - 1
        
print(output)






