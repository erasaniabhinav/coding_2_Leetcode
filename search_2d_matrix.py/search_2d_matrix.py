# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# # Output: true

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target = 10
# # for i in matrix:
# #     for j in i:
# #         #print(j)
# #         if j == target:
# #             print(True)
# #             break      
# flattening the 2d matrix to list 
flattened_matrix = [element for row in matrix for element in row]

target = 10

l = 0
r = len(flattened_matrix) - 1

while l <= r:
    mid = (l+r)//2

    if flattened_matrix[mid] == target:
        print(True)
        break
    elif flattened_matrix[mid] > target: 
        r = mid -1
    else:
        l = mid + 1

else: 
    print(False)
