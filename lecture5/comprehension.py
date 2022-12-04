l = [1, 2, 3, 4]
l2 = []

for n in l:
    l2.append(n ** 2)

l3 = [n ** 2 for n in l]

l4 = {str(n) : n ** 2 for n in l}

l5 = {}
for n in l:
    l5[ str(n) ] = n ** 2
