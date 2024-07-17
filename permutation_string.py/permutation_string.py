# Input: s1 = "abc", s2 = "lecabee"
# Output: true

s1 = "abc"
s2 = "lecabee"

# importing itertools module
import itertools

#initializing output to false 
output = False

# Generate all possible permutations of the string using this func
permutations = itertools.permutations(s1)

#print(permutations)

# Convert each permutation tuple to a string and store in a list
permutation_list = [''.join(p) for p in permutations]


print(permutation_list)

#checking if s2 has any of s1 
for i in permutation_list:
    if i in s2:
        output = True


print(output)