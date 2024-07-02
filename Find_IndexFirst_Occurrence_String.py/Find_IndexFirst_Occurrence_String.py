# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

haystack = "sadbutsad"
needle = "sad"

# #will use find method in python
# #searching for needle's index in haystack 
# output = haystack.find(needle)

# #print the first occurence
# print(output)


#for printing all the indexes
start = 0
output = []

#we need a loop here to iterate
while True:

    x = haystack.find(needle,start)

    #find will return -1 if no needle is found
    if x == -1:
        #in that case we break 
        break 

    #if needle is found we add that index to output
    # we store all the indices found in ouput    
    output.append(x)

    #and next interation will be from the element next to it
    start = x + 1

print(output)
#now the first occurence
print(min(output))