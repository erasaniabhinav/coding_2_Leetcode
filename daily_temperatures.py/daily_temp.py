# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

temperatures = [30,38,30,36,35,40,28]

#initialize an array to size of temp
#this way we maintain zeros if no higher temp is found
output_stack = [0]*len(temperatures)

#iterating through temp
for i in range(len(temperatures)):
     for j in range(i+1, len(temperatures)):
         if temperatures[j] - temperatures[i] > 0:
            #we add it at the index of the element in temp, in output_stack
            output_stack[i] = j-i
            #once we found a higer temp we update it 
            #and come out of it and move to next iteration
            break
        
        
print(output_stack)




  
    

