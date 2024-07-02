# Input: root = [5,1,4,null,null,3,6]
#[2,1,3]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4

#defined null as zero here 
null = 0

root = [2,1,3]

output = False

#checking if 5 is greater than 1 and 5 is > 4 in this
#first index > second and third
if root[0] > root[1] and root [0] < root[2]:
    output = True


print(output)