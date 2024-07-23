# Input: n = 1  
# Output: ["()"]
# Input: n = 3 
# Output: ["((()))","(()())","(())()","()(())","()()()"]
 
n = 3

result = []

curr = []
open = 0
close = 0

if len(curr) == 2 * n:
    result.append("".join(curr))
    
elif open < n:
    curr.append("(")
    open += 1
elif close < open:
    curr.append(")")
    close += 1

print(result)