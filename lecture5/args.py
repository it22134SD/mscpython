"""
Function argument types
"""
def add1(a, b = 1):
    return a + b

z = add1(1, 2)
print('z = ', z)

w = add1(1)
print('w = ', w)

p = add1(a = 1, b = 3)
print('p = ', p)
