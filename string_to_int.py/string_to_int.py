# Input: s = "1337c0d3"
# Output: 13373

import re 

s = "1337c0d3"

#initialize an empty list
output = []

#create a regex expression that matches 
x = r'[a-zA-Z0]'

#for evert element in s
for i in s:
    #if it is not in regex
    #re.match checks if x has i or not
    if not re.match(x,i):
        #appends all the values not in x
        output.append(i)

print(output)
#join list of strings together using .join
y = ''.join(output)    

print(y)


