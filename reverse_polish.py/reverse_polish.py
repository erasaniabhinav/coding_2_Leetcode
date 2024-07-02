# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6

def calculate(operator, item1 , item2):
    if operator == '+':
        return item1 + item2
    elif operator == '-':
        return item1 - item2
    elif operator == '*':
        return item1 * item2
    elif operator == '/':
        return item1 / item2


tokens = ["2","1","+","3","*"]

output = []

hash_symbol = ["+", "-","*","/"]

for i in range(len(tokens)):
    if tokens[i] not in hash_symbol:
        output.append(tokens[i])
    else:
        a = int(output.pop())
        b = int(output.pop())
        output.append(str(calculate(tokens[i], b, a)))
   

print(output[0])



