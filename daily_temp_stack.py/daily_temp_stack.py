# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

temperatures = [30,38,30,36,35,40,28]

#initialized to zeros to store the values 
#output = [0,0,0,0,0,0,0]
output = [0]*len(temperatures)

#empty list 
stack = []

#iterating through every index
for i in range(len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]: 
        x = stack.pop()
        output[x] = i - x

    stack.append(i)

print(output)






