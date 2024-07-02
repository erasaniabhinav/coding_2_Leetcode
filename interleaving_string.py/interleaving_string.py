# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

x = []
y = []

for i in s1:
    if i in s3:
        x.append("true")
    else:
        x.append("false")

for  j in s2:
    if j in s3:
        y.append("true")
    else:
        y.append("false")


print(x)
print(y)

#or can sort s1,s2,s3 and simply check if s1 and s2 are present in s3
