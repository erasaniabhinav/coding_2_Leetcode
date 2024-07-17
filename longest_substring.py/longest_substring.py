# Input: s = "zxyzxyz"
# Output: 3

s = "zxyzxyz"

#initilaize an empty list output
output = []

#iterating through s for every element
for i in s:
    #if the value is not in output
    if i not in output:
        #we add to to the output
        output.append(i)


#printing length gives the maximum length of the string without repeating
print(len(output))