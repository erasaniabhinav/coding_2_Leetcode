# Input: s = "the sky is blue"
# Output: "blue is sky the"

s = "the sky is blue"

#first we reverse the given string
a = s[::-1]

#print(a)

#now we split the reversed string
split_words = a.split()

#print(split_words)

#initilaize an empty array
output_string = [] #[i[::-1] for i in split_words]

for i in split_words:
    output_string.append(i[::-1])

#print(output_string)

# Join the reversed words back into a single string
output_strings = " ".join(output_string)

print(output_strings)