# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


x = 121 
#convert the given x to string
x = str(x)

#now we do string reversal and check if they both are same
if x == x [::-1]:
    print("x is palindrome")
    #else not a palindrome
else:
    print("x is not a palindrome")