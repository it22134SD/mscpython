from user import user, userdb

a = userdb()
a.connect()
a.update_name('Tom', 'thkam@hua.gr')
a.update_surname('Hanks', 'thkam@hua.gr')
a.update_password('hua', 'thkam@hua.gr')
