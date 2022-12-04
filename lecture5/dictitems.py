"""
Dict Example
"""
user = {'givenName' : 'Thomas',
        'surname' : 'Kamalakis',
        'email' : 'thkam@hua.gr',
        'phone' : '2109549406',
        'displayName' : 'Thomas Kamalakis' }

for key, val in user.items():
    print(key, ':', val)
