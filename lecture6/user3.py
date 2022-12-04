"""
User class
"""
from hashlib import sha256

#---user1
class user:

    def __init__(self, *args):
        # if there is one argument:

        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, dict):
                self.__set_user(arg['name'],
                                arg['surname'],
                                arg['email'],
                                arg['password'])

            elif isinstance(arg, list):
                self.__set_user(arg[0],
                                arg[1],
                                arg[2],
                                arg[3])
        elif len(args) == 4:
            self.__set_user(args[0],
                            args[1],
                            args[2],
                            args[3])
        else:
            raise TypeError('You need to supply a single argument that is either a list or a dict, or 4 string arguments ')
#---user2

    def __set_user(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.display_name = name + " " + surname
        self.set_password( password )

    def __str__(self):
        return self.display_name + ' (' + self.email + ')'

    # Update the user password hash
    def set_password(self,plain_text):
        h = sha256( plain_text.encode() )
        self.password = h.hexdigest()

    # verify password
    def verify_password(self, plain_text):
        h = sha256( plain_text.encode() )
        return self.password == h.hexdigest()

    # return as dictionary
    def as_dict(self):
        return {
            'name' : self.name,
            'surname' : self.surname,
            'email' : self.email,
            'display_name' : self.display_name,
            'password' : self.password
        }
