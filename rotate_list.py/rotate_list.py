# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

head = [1,2,3,4,5]
k = 2

output = []

# Calculate the start index from the beginning
start_index = len(head) - k

#the index of the element from start is 3


#now using list slicing 
output = head[start_index:]+ head[0:start_index]      

print(output)