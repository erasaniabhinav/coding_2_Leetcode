# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

nums = [1,2,4,6]

#lets initialize an empty list
output = []

#we now calculate the product of nums and store it in x 
x = 1

#itearte through nums
for i in (nums):
    #store the product
    x = x * i 

print(x)    

#again in here we divide the product with every element in nums
for j in nums:
    output.append(x//j)

#this way it gives product of everything except that index number    
print(output)
