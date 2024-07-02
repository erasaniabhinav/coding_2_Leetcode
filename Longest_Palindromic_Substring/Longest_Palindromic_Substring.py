# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

s = "babad"

#initialize two lists x,y 
x = []
y = []

#in range of s
for i in s:
    #add element at every index one by one to x
    x.append(i)
    #after adding we check if x is same after reversing it
    if x == x[::-1]:
        print(x)
     
        # print(x)
        # print((len(x)))
        #add the length of x == reverse of x to y
        y.append(len(x))

#print the max possible length
print(max(y))