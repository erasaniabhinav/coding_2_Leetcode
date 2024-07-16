# Input: s = "Was it a car or a cat I saw?"
# Output: true

#s = "Was it a car or a cat I saw?"

# #will split the string on spaces and then rejoin it
# x= "".join(s.split(" "))

# #strip the last element
# x = x.rstrip("?")
# print(x)
# #lower case the entire string 
# x = x.lower()

# #check if x equals reverse 
# if x == x[::-1]:
#     print(True)
# else:
#     print(False)

#x = s.rstrip("?")

s = "Was it a car or a cat I saw?"

#remove spaces
x= "".join(s.split(" "))
x = x.rstrip("?")
#convert to lower 
x = x.lower()

l = 0
r = (len(x)-1)

# Assume it is a palindrome initially
palindrome = True

while l <= r:
    if x[l] != x[r]:
        palindrome = False
        break
    l += 1
    r -= 1

print(palindrome)


