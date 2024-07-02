# Input: l1 = [2,2,5], l2 = [5,6,4]
# Output: [7,8,9]


#take the input
l1 = [2,2,5]
l2 = [5,6,4]

#initialize an array for output
output = []
#i in range of length l1
for i in range(len(l1)):

    #append the values at index i in both l1 and l2
    output.append(l1[i]+l2[i])

print(output)

