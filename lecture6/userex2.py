# import the user class
from user import user

a = user('Thomas', 'Kamalakis', 'thkam@hua.gr', 'hua123')
b = user(['Thomas', 'Kamalakis', 'thkam@hua.gr', 'hua123'])
c = user({ 'name' : 'Thomas',
           'surname' : 'Kamalakis',
           'email' : 'thkam@hua.gr',
           'password' : 'hua123'
})

print(a)
print(b)
print(c)
