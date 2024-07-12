# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Input: prices = [10,8,7,9,11,5,2]

# Output: 9

# prices = [10,8,7,9,11,5,2]

# #initialize an empty list 
# output = []

# #itearting through the given input
# for i in range(1,(len(prices)-1)):
#     #checking if prices are same at before and after index of i
#     if prices[i] > prices[i-1] and prices[i+1]>prices[i]:
#         output.append(prices[i])

# print(max(output))

# Input: nums = [4,5,6,7,0,1,2]
# target = 0
# Output: 4

# nums = [4,5,6,7,0,1,2]
#        #0,1,2,3,4

# target = 2

# #iterate through given nums
# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# nums = [5,7,7,8,8,10]
# target = 7

# output = []

# for i in range(len(nums)):
#     if nums[i] == target:
#         output.append(i)


# print(output)

# output =  [0,1,1,2,3,5,8,13,21]

# a = 0
# b = 1

# input =  [0,1,1,2,3,5,8,13,21]

# output = input [-1] + input[-2]

# print(output)

# a = 0 
# b = 1

# c = a + b
