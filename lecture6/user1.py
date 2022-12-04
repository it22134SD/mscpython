"""
User class
"""
from hashlib import sha256

#---userstart
class user:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.display_name = name + " " + surname
        self.set_password( password )
#---initend
#---strstart
    def __str__(self):
        return self.display_name + ' (' + self.email + ')'
#---strend
#---setpassword1
    # Update the user password hash
    def set_password(self,plain_text):
        h = sha256( plain_text.encode() )
        self.password = h.hexdigest()
#---setpassword2

#---checkpassword1
    # verify password
    def verify_password(self, plain_text):
        h = sha256( plain_text.encode() )
        return self.password == h.hexdigest()
#---checkpassword2

#---asdict1
    def as_dict(self):
        return {
            'name' : self.name,
            'surname' : self.surname,
            'email' : self.email,
            'display_name' : self.display_name
#            'password' : self.password
        }
#---asdict2
