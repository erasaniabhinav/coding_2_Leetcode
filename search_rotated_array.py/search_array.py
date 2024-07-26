# Input: nums = [3,4,5,6,1,2], target = 1
# Output: 4


nums = [3,4,5,6,1,2]
target = 1

# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)

l = 0
r = len(nums)-1

while l < r:
    mid = (l+r)//2
    
    if nums[mid] == target:
        result = (mid)
        break

    if nums[mid] > nums[l]:
        l = mid + 1
    else:
        r = mid - 1

print(result)