# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3

dividend = 10
divisor = 3

#initialize an empty list 
output = []


#divide the given and assign it to output
output = dividend/divisor

#print(output)
#we will round the output using round function
print(round(output))