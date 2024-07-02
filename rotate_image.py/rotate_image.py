# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


matrix = [[1,2,3],[4,5,6],[7,8,9]]

output = []

#we take sublists in given matrix and form a separate list
#first index 
first_elements = [i[0] for i in matrix]
#for index 1
second_elements = [i[1] for i in matrix]
#for index 2
thrid_elements =  [i[2] for i in matrix]

#reverse the sublists within a nested list
x = first_elements[::-1]
y = second_elements[::-1]
z = thrid_elements[::-1]

#append them to output
output.append([x,y,z])


print(output)