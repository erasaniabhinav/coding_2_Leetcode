# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4]

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

digits = [4,3,2,1]

#first we slice from start to last but one element
output = digits[0:-1]

#next we append the last element + 1
output.append(digits[-1] + 1)

#print(output)
print(output)