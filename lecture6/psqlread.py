from user import user, userdb

a = userdb()
a.connect()
u = a.get_user('thkam@hua.gr')
print(u)
