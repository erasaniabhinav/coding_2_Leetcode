# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

s = "()[]{}"

parenthesis = {")":"(","]":"[","}":"{"}

#create an empty list to add and check for matching
stack = []

#iterating through every element
for i in s:
    #check if the element is in keys of parenthesis
    if i in parenthesis:
        #and checking is stack is not empty and last element in stack os equal to value of parenthesis
        if stack and stack[-1] == parenthesis[i]:
            #if it matches we make the stack empty for next iteration
            stack.pop()
        #else: we add it if it matches key but does not have a value in stack    
        else:
            stack.append(i)
    #we add to stack if i is not in keys of parenthesis as well
    else:
        stack.append(i)
#finally we check if the stack is empty or not 
if len(stack)==0:
    print("True")
else:
    print("False") 