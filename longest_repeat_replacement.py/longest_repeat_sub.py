# Input: s = "XYYX", k = 2
# Output: 4

s = "XYYX"
k = 2


output = []

for i in s:
    if i != "X":
        output.append("x")
    else:
        output.append(i)

print(len(output))