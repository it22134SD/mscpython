import csv

csv_input = open('users.csv')
csv_reader = csv.reader(csv_input, delimiter=';')

csv_output = open('users_out.csv' , 'w')
csv_writer = csv.writer(csv_output, delimiter = ';')

line_count = 0
for row in csv_reader:
    if line_count == 0: #Header line
        write_row = ['givenName', 'surname', 'displayName', 'email', 'phone']
    else:
        display_name = row[0] + " " + row[1] + " (" + row[2] + ")"
        write_row = [row[0], row[1], display_name, row[2], row[3] ]
    line_count = line_count + 1
    print(write_row)
    csv_writer.writerow(write_row)

csv_input.close()
csv_output.close()
