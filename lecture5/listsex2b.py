"""
List example
"""

original = ["Thomas", "Kamalakis", "automation"]
final = ["Tom", "Camalakis", "telecom"]
str_input = "Thomas Kamalakis is teaching a course on automation"
str_output = str_input

for i, orig in enumerate(original):
    print('In iteration:', i,' replacing ',orig,' with ',final[i])
    str_output = str_output.replace( orig, final[i] )

print('Original string: ', str_input)
print('Final string: ', str_output)
