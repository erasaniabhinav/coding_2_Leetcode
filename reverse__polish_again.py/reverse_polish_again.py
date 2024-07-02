# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6

tokens = ["2", "1", "+", "3", "*"]

output = []

hash_symbols = ["*", "-", "+", "/"]

#iterating through every element in tokens
for token in tokens:
    #if elment is not in symbols then it is understood that it is an int
    if token not in hash_symbols:
        #now we add the int of it
        output.append(int(token))
    else:
        #now we have two elements in output
        #we store the two values in a and b and then perform the calculation
        b = output.pop()
        a = output.pop()
        if token == "+":
            output.append(a + b)
        elif token == "-":
            output.append(a - b)
        elif token == "*":
            output.append(a * b)
        elif token == "/":
            output.append(a / b)

print((output[0]))

