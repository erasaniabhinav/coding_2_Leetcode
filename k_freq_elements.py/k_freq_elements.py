# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

nums = [1,2,2,3,3,3]

k = 2

#we put an empty list in here to store the values
x = []

#iterating through the nums
for i in nums: # O(n)
    #checking if the count of every element in the list is >= to k
    if nums.count(i) >= k: #O(n)
        x.append(i)

#might add the same elements again
#use set to remove the duplicates
print(list(set(x)))
