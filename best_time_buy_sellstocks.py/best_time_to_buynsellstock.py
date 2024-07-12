#best time to buy and sell stock 

prices = [10,1,5,6,7,1]

# Output: 6
#initialize an empty list
output = []

#iterate through the given prices
#from second element to last but one 
for i in range(1,(len(prices) - 1)):
    #now we check if the element before i is less than i
    #and element after i is greater than i,only then we get profit
    if prices[i] > prices[i-1] and prices[i+1]>prices[i]:
        #add them to output
        output.append(prices[i])

#we print the maximum value, indicating max profit
print(max(output))