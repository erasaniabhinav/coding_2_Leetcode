# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6

nums = [1,2,3,1]

#now we find the max in the list first
x = max(nums)

#while iterationg through the list
for i in range(len(nums)):
    #if we find the max of list 
    #then we return the index at which it was found
    if nums[i] == x :
        print(i)