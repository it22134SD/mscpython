import csv

csv_file = open('users.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter = ';')

users = []          # Initialize empty list
line_count = 0
for row in csv_reader:
    if line_count == 0:
        pass
    else:
        d = {
            'givenName' : row[0],
            'surname' : row[1],
            'email' : row[2],
            'phone' : row[3]
        }
        users.append( d ) # add to user list
    line_count += 1
print(users)
csv_file.close()
