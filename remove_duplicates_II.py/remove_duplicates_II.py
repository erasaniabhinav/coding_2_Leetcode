# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]

nums = [1,1,1,2,2,3]

output = []

#iterating through nums
for i in nums:
   
   #here we write two conditions the first is we see if i is not in output
   #and the numbers should repeat only twice in output so we count it (#0 and 1)
   if i not in output or output.count(i) <= 1:
        output.append(i)

print(output)
print(len(output))