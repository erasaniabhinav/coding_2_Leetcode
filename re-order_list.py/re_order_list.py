# Input: head = [2,4,6,8]
# Output: [2,8,4,6]
# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]

head = [2,4,6,8,10]
# [0, n-1, 1, n-2, 2, n-3, ...]

output = []

# No need to rearrange if the list has 0 or 1 element
if len(head) <= 1:
    print(head)

l = 0 
r = len(head) -1 

#while left is less than right
while l <= r:
    # in this case there is only one element left as l == r
    if l == r:
        output.append(head[l])
    else:
        #if l not equal to r then we add left value first and then right
        #and then we continue adding them 
        output.append(head[l])
        output.append(head[r])
    #after every itearation we move the pointers 
    l += 1
    r -= 1

print(output)

#O(n) because each element is processed exactly once




