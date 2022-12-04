from budi import budiapi
b = budiapi()
r = b.search_rows('personnel', 'HRMS',
                 {'title': 'Professor' } )
print(r)

r = b.search_rows('personnel', 'HRMS',
                 {'surname': 'Kamalakis' } )
print(r)
