"""
Variable Scope
"""
my_var = 10 # global variable

def test():
    y = 30          # local scope, y is not known outside of test()
    print('my_var = ', my_var)
    print('y = ', y)

def test2():
    global x        # x is declated as global!
    x = 20

test()
test2()
print('x = ',x)
print('y = ',y) # this produces an error!
