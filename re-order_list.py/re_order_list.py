# Input: head = [2,4,6,8]
# Output: [2,8,4,6]

# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]


head = [2,4,6,8,10]
 

x = head[3]
head.pop()

print(head)
head.insert(1,x)

print(head)


