import csv
users = []              # Initialize empty list

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ';')
    keys = next(csv_reader) # Keys are located on the first row

    for row in csv_reader:
        d = {}            # Empty dictionary
        for i, k in enumerate(keys):
            d[k] = row[i]
        users.append( d ) # add to user list
print(users)
# No need to close csv_file !
