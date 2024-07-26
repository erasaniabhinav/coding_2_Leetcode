# Input: piles = [1,4,3,2], h = 9
# Output: 2

piles = [1,4,3,2] 
h = 9
k = 2

output = 0



for i in piles:
    output += i // k 

    if i % k != 0:
        output += 1


print(output)

#min val of k is 1 and max is 4, as the max number of bananas is 4 

