# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

head = [1,2,3,4,5]
n = 2

#removing the 2nd element from the end of the list using pop
output = head.pop(-n)

#printing output and head to see the result
print(output)
print(head)