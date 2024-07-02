# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

x = 1

for i in range(5):
    for j in range(i+1,5):
        print(x,end = " ")
