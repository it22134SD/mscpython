"""
String in String
"""

S = "Thomas Kamalakis"
s = "Thomas"
if s in S:
  print(s, 'is contained in', S)
else:
  print(s, 'is not contained in', S)    

s2 = "Tom"
if s2 in S:
  print(s2, 'is contained in', S)
else:
  print(s2, 'is not contained in', S)
