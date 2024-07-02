# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#given list of strings
strs = ["flower","flow","flight"]

#initialize an empty list
s = []

#sort strs to get the shortest one first 
strs.sort() 

#len of shortest
l = strs[0]


#as long as the length of shortest string
for i in range(len(l)):
    #if the letters are same for the first and last strings in every iteration
    if strs[0][i]== strs[-1][i]:
        #we add them to s
        s.append(strs[0][i])


print(s)