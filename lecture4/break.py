"""
break example
"""
S = 0
a = input('Please give a number: ')
while a != 'STOP':
    num = float(a)
    print(num)
    if num < 0:
        break
    S = S + num
    print('Sum is: ', S)
    a = input('Please give a number: ')
