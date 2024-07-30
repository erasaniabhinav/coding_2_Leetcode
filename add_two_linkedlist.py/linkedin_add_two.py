# Input: l1 = [1,2,3], l2 = [4,5,6]
# Output: [5,7,9]
# Explanation: 321 + 654 = 975.

l1 = [1,2,3]
l2 = [4,5,6]

# Initialize an empty list to store the result
output = []


# Initialize two pointers for traversing the lists
l = 0
r = 0

# Iterate while both pointers are within the bounds of their respective lists
while l < len(l1) and r < len(l2):
    #elements from both lists to the output list
    output.append(l1[l]+l2[r])
    
    # Increment the pointers to move to the next elements in the lists
    l += 1
    r += 1

print(output)
