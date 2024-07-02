# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations


candidates = [2,3,6,7]
target = 7

#initialize an empty list to store the possible values during iteration
output = []

#i, j , k iterates through the candiates and checks for all 
#possibilities so that they add up to target
for i in candidates:
    for j in candidates:
        for k in candidates:
            #if matches target we add it to output
            if i + j + k == target:
                output.append([i,j,k])


#sort them in asceding and pick the small one(3 same combinations in this case)#
x = sorted(output)

for y in candidates:
    if y == target:
        output.append([y])


print(x[0],output[-1])