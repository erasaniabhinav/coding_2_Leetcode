# Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]
# Input: head = [5], n = 1
# Output: []


head = [5]
n = 1

# Checking if n is a valid index
if 0 <= n <= len(head):
    head.pop(-n)
else:
    print("[]")


print(head)
#The overall time complexity is dominated by the pop operation, which is O(n)