# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]

# # Concatenating two lists of lengths n,m : O(n+m)
# output = list1 + list2

# #sorting has O((n+m)log(n+m))
# output.sort()
# print(output)

list1 = [1,2,4]
list2 = [1,3,5]

output = []

l = 0
r = 0


# Loop until we reach the end of either list1 or list2
while l < len(list1) and r < len(list2):
    if list1[l] <= list2[r]:
        output.append(list1[l])
        l += 1
    else: 
        output.append(list2[r])
        r += 1


# If there are remaining elements in list1, append them to output_stack
while l < len(list1):
    output.append(list1[l])
    l += 1

# If there are remaining elements in list2, append them to output_stack
while r < len(list2):
    output.append(list2[r])
    r += 1

print(output)