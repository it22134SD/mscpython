"""
For and if example
"""
names = ['Alice', 'Bob', 'Eve']
for x in names:
    print(x)
    sf = x.upper()
    # sr = x[::-1].upper()
    sr = sf[::-1]
    if sf == sr:
        print(x, 'is palindrome!')
    else:
        print(x, 'is not palindrome')
