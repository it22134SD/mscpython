# Import Python's csv module
import csv

# Open the users csv file
csv_file = open('users.csv')

# Invoke the csv reader and use ";" as delimiter
csv_reader = csv.reader(csv_file, delimiter = ';')

# Iterate through the rows of the file
for row in csv_reader:
    print(row)  # row is a LIST!
    for column in row:
        print(column)
csv_file.close()
