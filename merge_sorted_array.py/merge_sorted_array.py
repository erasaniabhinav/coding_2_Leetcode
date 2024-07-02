# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]

nums1 = [0]
nums2 = [1]

output = []

#we concatenate two given lists
x = nums1+nums2

#sort it asceding
x.sort()

for i in x:
    #we remove 0's from it
    if i != 0:
        #append it to output
        output.append(i)

print(output)