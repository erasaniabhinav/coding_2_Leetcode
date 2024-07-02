# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

s = "   fly me   to   the moon  "

#removes the starting and ending spaces in the string initally
a = s.strip()

#split the given string using split(" ")
#now we split it on spaces
new_word = a.split(" ")

print(new_word)


#we now print the length of the last word in the list 
print(len(new_word[-1]))

