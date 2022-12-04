import csv

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ';')
    keys = next(csv_reader) # Keys are located on the first row

    users = [ {k : row[i] for i, k in enumerate(keys) } for row in csv_reader ]
print(users)
# No need to close csv_file !
