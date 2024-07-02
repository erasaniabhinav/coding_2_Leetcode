# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

head = [1,2,3,4,5]

new_element = head[-1]
new_element_2 = head[-2]

#we pop the last element first and then second last
head.pop(-1)
#now last element is 4, as we have popped out 5
head.pop(-1)

#then using insert method in python we insert where ever we want 
head.insert(1,new_element)
head.insert(3,new_element_2)

print(head)

