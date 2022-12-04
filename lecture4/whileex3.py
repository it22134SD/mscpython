"""
While loop example
"""
import time
S = 0
#a = input('Give me a number: ')
a = 'h'*10000
while a != "STOP":
    t1 = time.time()
    count_dots = 0

    is_number = True
    for ch in a:
        if ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ,'.']:
            is_number = False
        if ch == '.':
            count_dots += 1

    if is_number and (count_dots <=1):
        S = S + float(a)
        print('Sum is:', S)
    else:
        print('You have not given me a number!')
    t2 = time.time()
    print('Elapsed time', t2-t1, 'secs')

    a = input('Give me a number: ')
