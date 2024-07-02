# Input: s = "III"
# Output: 3
# Explanation: III = 3

#create a dictionary to store the corresponding values
rom_int = {"I":1,"V":5,"X":10,"L":50}

s = "LVIII"

#initialize output to empty list
output = []

#for every element at index in s
for i in s:
    #if it matches keys in dict rom_int
    if i in rom_int:
        #we append its value to output
        output.append(rom_int[i])

#print the sumof it
print(sum(output))

