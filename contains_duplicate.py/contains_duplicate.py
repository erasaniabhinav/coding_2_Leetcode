# Input: nums = [1, 2, 3, 3]

# Output: true

nums = [1, 2, 3, 4, 5]

# #lets first take output as false 
output = False 

#initiliaze an empty list 
x = []

#itearating through 
for i in nums:
    #initially if element is not in x
    if i not in x:
        #we add it to x 
        x.append(i)
    #if the new element is already in x
    #it means it has a duplicate
    else:
        #we change the output to true
        output = True

print(output)


# # Input: strs = ["act","pots","tops","cat","stop","hat"]

# # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# strs = ["act","pots","tops","cat","stop","hat"]

# x = {}

# for i in strs:                              
    
#     y = ''.join(sorted(i))
#     print(y)
#     if y in x:
#         x[y].append(i)
#     else:
#         x[y] = [i]

# print((x.values()))






























