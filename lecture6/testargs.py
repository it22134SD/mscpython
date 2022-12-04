def test(*a):
    if len(a) == 1:
        v = a[0]
        if isinstance(v, list):
            print('List : ', v)
        elif isinstance(v, dict):
            print('Dict :', v)
    else:
        print(a)

test(1, [1,2], {'a':1, 'b' : 2})
test([1,2])
test({'a' : 1, 'b' : 2})
