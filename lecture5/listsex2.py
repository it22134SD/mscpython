"""
List example
"""

original = ["Thomas", "Kamalakis", "automation"]
final =    ["Tom",    "Camalakis", "networks"]
str_input = "Thomas Kamalakis is teaching a course on automation"
str_output = str_input

for i in range( len(original) ):
    str_output = str_output.replace( original[i], final[i] )

print('Original string: ', str_input)
print('Final string: ', str_output)
