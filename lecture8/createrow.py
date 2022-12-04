from budi import budiapi
b = budiapi()
r = b.create_row('personnel', 'HRMS',
                 {'notes': 'nada',
                  'title': 'Professor',
                  'department': 'Informatics and Telematics',
                  'idNumber': '12345',
                  'surname': 'Ayiannis',
                  'givenName': 'Yiannis' })
print(r)
