# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

nums = [100,4,200,1,3,2]

nums.sort()

print(nums)

#we put output = 1 as we know that first element is 1
output = [1]

#in every itearation
for i in range(len(nums)):
    # we check if first element + 1 is equal to next element 
    if nums[i] + 1 == nums[i+1]:
        #we append to output
        output.append(1)
    #if the next element is not +1 of previous, stop it 
    else:
        break

print(output)

#finally now we print the length
print(len(output))


