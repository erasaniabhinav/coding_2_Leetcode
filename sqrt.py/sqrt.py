# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned

#import math library
import math 

x = 8

#math.floor rounds off to base nearest integer 
output = math.floor(math.sqrt(8))

print(output)