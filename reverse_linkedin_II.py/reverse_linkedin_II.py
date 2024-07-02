# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

head = [1,2,3,4,5]

output = []

#iterate through head list
for i in head:
    #if it matches 2 then we change its value to 4
    if i==2:
        output.append(4)
    #if it matches 4 then we change its value to 2
    elif i==4:
        output.append(2)
    #if not equal to 4 or 2 then we add them also
    else:
        output.append(i)

print(output)
