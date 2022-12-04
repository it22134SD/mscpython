from user import user, userdb

a = userdb()
a.connect()

users = a.all_users()
print(users)

a.export_to_csv('users.csv')
a.close()
