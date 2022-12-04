"""
User class
"""

#---userstart
class user:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.display_name = name + " " + surname
#---initend
#---strstart
    def __str__(self):
        return 'User object: ' + self.display_name + ' (' + self.email + ')'
#---strend
