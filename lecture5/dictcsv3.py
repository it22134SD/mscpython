import csv

csv_file = open('users.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter = ';')

users = []              # Initialize empty list
keys = next(csv_reader) # Keys are located on the first row

for row in csv_reader:
    d = {}      # Empty dictionary
    for i, k in enumerate(keys):
        d[k] = row[i]
    users.append( d ) # add to user list
print(users)

csv_file.close()
