from user import user, userdb

a = userdb()
a.connect()
u = user('Tom', 'Kamalakis', 'thkam@hua.gr', 'hua123')
a.insert_user(u)
a.close()
