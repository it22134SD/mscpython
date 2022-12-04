"""
Function examples
"""

def add(a, b):
    return a + b

def user_dict(givenName, surname, email, phone):
    displayName = givenName + " " + surname
    return {
        'givenName' : givenName,
        'surname' : surname,
        'email' : email,
        'phone' : phone,
        'displayName' : displayName
    }

c = add(1, 2)
print(c)
user = user_dict('Thomas', 'Kamalakis', 'thkam@hua.gr', '2109549406')
print( user )
