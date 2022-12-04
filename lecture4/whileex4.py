import time

"""
While loop example
"""
S = 0
#a = input('Give me a number: ')
a = 'h'*10000
while a != "STOP":
    t1 = time.time()
    try:
        S = S + float(a)
        print('Sum is:', S)

    except ValueError:
        print('You have not given me a number!')
    t2 = time.time()
    print('Elapsed time', t2-t1, 'secs')
    a = input('Give me a number: ')
