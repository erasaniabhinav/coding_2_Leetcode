# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]

numbers = [1,2,3,4]
target = 3

# #iterating through numbers twice and then 
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
          # #checking if numbers add up to target
#         if numbers[i] + numbers [j] == 3:
#             print(numbers[i] , numbers [j])

l = 0
r = l+1

#while left pointer is less then or equal to right
while l <= r:
    #checking if numbers add up to target
    if numbers[l] + numbers[r] == target :
        print(numbers[l],numbers[r])
        break
    #or we will increment the pointers
    else:
        l += 1
        r += 1