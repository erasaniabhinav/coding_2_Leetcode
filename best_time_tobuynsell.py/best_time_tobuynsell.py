# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6


prices = [10,1,5,6,7,1]

#initilaize an empty list to store values
output = []

#itearating from 1 to last but 1 in prices
#so that there is always an element before and after index i
for i in range(1,len(prices)-1):
    #checking if previous num is less than and next num is greater than index i element value
    if prices[i] > prices [i-1] and prices [i] < prices [i+1]:
        output.append(prices[i])

#max profit
print(max(output))