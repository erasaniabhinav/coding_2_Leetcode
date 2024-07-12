# Input: s = "racecar", t = "carrace"

# Output: true

s = "racecar"
t = "carrace"

#initliaze output to false 
output = False

#by sorting the two strings we should get the same string if they are 
#anagrams
a = sorted(s)
b = sorted(t)

print(a,b)

#check a and b 
if a == b:
    #change the output to true 
    output = True

print(output)