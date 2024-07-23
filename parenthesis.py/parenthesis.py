# Input: s = "([{}])"
# Output: true

s = "[(])"

#initialize an empty stack to store elements and check the condition
stack = []

#matching parenthesis are put in a dictionary
dict_match = {")":"(","}":"{","]":"["}

for i in s:
    #if i is not in dict then we add it to stack and we get ['(', '[', '{']
    if i not in dict_match:
        stack.append(i)
    else:
        #now if i matches the value of key in dict 
        #we compare it with last element in stack to make it valid
        if dict_match[i] == stack [-1]:
            #if mathces then we remove the pair 
            stack.pop(-1)

print(stack)

#if its empty that means every parenthesis has a matching closing one
if len(stack) == 0:
    print(True)
else:
    print(False)