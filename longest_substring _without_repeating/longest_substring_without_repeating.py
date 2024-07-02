# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1

s = "bbbbb"

#initialize to zero
output = 0
#initialize empty list
x = []

#values at every index
for i in s:
    #add elements in s to x if they are not already in x
    if i not in x:
        x.append(i)
        #increase output count by 1 after adding every element
        output += 1
    else:
        #if same element is already in x after adding, we stop
        break

print(output)


