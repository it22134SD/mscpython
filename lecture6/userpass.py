# import the user class
from user1 import user

# create a user object
a = user('Thomas', 'Kamalakis', 'thkam@hua.gr', 'hua123')

check = a.verify_password('hua')
print(check)

check = a.verify_password('hua123')
print(check)
