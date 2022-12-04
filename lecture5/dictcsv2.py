import csv

csv_file = open('users.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter = ';')

users = []          # Initialize empty list
line_count = 0
for row in csv_reader:
    if line_count == 0:
        keys = row
        print('Read Headers:', keys)
    else:
        d = {}      # Empty dictionary
        for i, k in enumerate(keys):
            d[k] = row[i]
            print('Line ', line_count, k, ':', row[i])
        users.append( d ) # add to user list
    line_count += 1
print(users)

csv_file.close()
