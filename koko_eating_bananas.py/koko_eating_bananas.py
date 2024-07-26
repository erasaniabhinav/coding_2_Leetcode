# Input: piles = [1,4,3,2], h = 9
# Output: 2

#there are 4 piles of bananas here

piles = [1,4,3,2]
h = 9
#The minimum eating speed is 1 banana per hour.
k = 2

output = 0

#iterating through piles  
for i in piles:
    # if every element gets divided by k correctly leaving 0 remainder
    # we add the quotient to the sum 
    output += i // k 

    #if the koko can not complete pile in 1 hr at speed k
    # then we add 1 to output as it takes 1 more hr extra 
    if i % k != 0:
        output += 1


    # print(output)





print("final hrs :", output)


