"""
While loop example
"""
S = 0
a = input('Give me a number: ')
while a != "STOP":
    S = S + float(a)
    print('Sum is:', S)
    a = input('Give me a number: ')
