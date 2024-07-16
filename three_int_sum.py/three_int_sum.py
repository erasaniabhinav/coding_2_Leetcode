# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]

output = []

nums.sort()

#iterate through each possible first element
for i in range(len(nums)-2):
    #it means the number is repeating
    if i > 0 and nums[i] ==  nums [i-1]:
        continue

    
    l = i + 1
    r = len(nums)-1

    while l < r :
        total = nums[i] + nums[l] + nums[r]

        if total == 0:
            output.append([nums[i],nums[l],nums[r]])
            #skipping duplicates by checking the indices 
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            #skipping duplicates by checking the indices
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            l += 1
            r -+ 1
        elif total < 0:
            l += 1
        else:
            r -= 1

print(output)





