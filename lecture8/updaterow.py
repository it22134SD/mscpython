from budi import budiapi
b = budiapi()

r = b.update_row('personnel', 'HRMS',
                 {'surname': 'Kamalakis' },
                 {'surname' : 'Kamos'})
print(r)
