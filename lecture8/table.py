from budi import budiapi
b = budiapi()
info = b.get_table_info('personnel', 'HRMS')
print(info)

data = b.get_table_data('personnel', 'HRMS')
print(data)
