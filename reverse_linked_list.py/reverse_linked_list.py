# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

head = [0,1,2,3]

# output = head[::-1]
# print(output) 
# the time complexity of this operation is O(n)

output = []

for i in head:
    #the insert method to add elements at specific positions within the stack
    output.insert(0,i)

print(output)
