# Input: nums = [2,2,1]
# Output: 1

# Input: nums = [4,1,2,1,2]
# Output: 4

nums = [4,1,2,1,2]

#output_stack = []

#first we sort the elements in alphabetical order, doesnt matter even if we dont
nums.sort()

print(nums)

#for every element in nums
for i in nums:
    #if count if it is equal to 1
    if nums.count(i) == 1:
        #then that is out single number and so we print it now
        print(i)