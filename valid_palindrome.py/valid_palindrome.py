# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome

s = "A man, a plan, a canal: Panama"
print(s)


#checks if the character is an alphabetic character
#concatenates the list of characters into a single string again
s_stripspaces_extras = ''.join([i for i in s if i.isalpha()])

print(s_stripspaces_extras)

#we change this to lower case 
y = s_stripspaces_extras.lower()

#check if it is same if we reverse it also
if y == y[::-1]:
    print(True)
else:
    print(False)