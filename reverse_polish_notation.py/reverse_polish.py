# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

tokens = ["1","2","+","3","*","4","-"]

#initialize an empty list to store the elements from tokens
result = []

#iterating through everyelement in tokens
for i in tokens:
    #if the element is digit, we add to result stack
    if i.isdigit():
        result.append(i)
    # if it is +     
    elif i == "+":
        #then we pop the last two elements int version to make calculations
        #store them in a & b 
        b = int(result.pop())
        a = int(result.pop())
        #perform the respective calculation
        result.append(a+b)
    elif i == "*":
        b = int(result.pop())
        a = int(result.pop())
        result.append(a*b)
    elif i == "-":
        b = int(result.pop())
        a = int(result.pop())
        result.append(a-b)
    elif i == "/":
        b = int(result.pop())
        a = int(result.pop())
        result.append(a/b)

print(result[0])




