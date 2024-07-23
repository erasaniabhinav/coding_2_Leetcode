# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

nums = [-1,0,2,4,6,8]

target = 4

#initlaize two pointers l and r 
l = 0
r = len(nums) - 1

#while length of l is less than right pointer 
while l <= r:
    # Calculate the middle index
    mid = (l + r)//2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        # Narrow down to the left half
        r = mid - 1
    else:
        # Narrow down to the right half
        l = mid + 1

else:
    print("not found")
    

