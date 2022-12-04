"""
User class
"""
from hashlib import sha256
import psycopg2
import csv

SERVER_IP = '192.168.56.102'
DB_NAME = 'userdb'
DB_USER = 'postgres'
DB_PASSWORD = 'hua123'
CSV_HEADERS = ['email', 'name', 'surname', 'password']

class user:

    def __init__(self, *args, hash_password = True):
        # if there is one argument:
        self.hash_password = hash_password

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

    def __set_user(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.display_name = name + " " + surname
        if self.hash_password:
            self.set_password( password )
        else:
            self.password = password

    def __str__(self):
        return self.display_name + ' (' + self.email + ')'

    def __repr__(self):
        return self.__str__()

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

class userdb:
    def __init__(self, server_ip = SERVER_IP,
                       db_name = DB_NAME,
                       db_user = DB_USER,
                       db_password = DB_PASSWORD ):

        self.server_ip = server_ip
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def connect(self):
        self.conn = psycopg2.connect(
                      host = self.server_ip,
                      database = self.db_name,
                      user = self.db_user,
                      password = self.db_password)

    def close(self):
        self.conn.close()

    def insert_user(self, user):
        cursor = self.conn.cursor()
        name = user.name
        surname = user.surname
        email = user.email
        password = user.password
        query = """INSERT INTO users (email, givenName, surname, password) VALUES ('%s', '%s', '%s', '%s') """ %(email, name, surname, password)
        print(query)
        cursor.execute(query)
        self.conn.commit()

    def get_user(self, email):
        cursor = self.conn.cursor()
        query = """SELECT * FROM users WHERE (email='%s') """ %email
        print(query)
        cursor.execute(query)
        if cursor.rowcount == 1:
            u = cursor.fetchall()[0]
            return user( u[1], u[2], u[0], u[3], hash_password = False )

    def update_name(self, name, email):
        cursor = self.conn.cursor()
        query = """UPDATE users SET givenName = '%s' WHERE email = '%s' """ %(name, email)
        cursor.execute(query)
        self.conn.commit()

    def update_surname(self, surname, email):
        cursor = self.conn.cursor()
        query = """UPDATE users SET surname = '%s' WHERE email = '%s' """ %(surname, email)
        cursor.execute(query)
        self.conn.commit()

    def update_password_hash(self, hash, email):
        cursor = self.conn.cursor()
        query = """UPDATE users SET password = '%s' WHERE email = '%s' """ %(hash, email)
        cursor.execute(query)
        self.conn.commit()

    def update_password(self, password, email):
        cursor = self.conn.cursor()
        hash = sha256( password.encode() ).hexdigest()
        query = """UPDATE users SET password = '%s' WHERE email = '%s' """ %(hash, email)
        cursor.execute(query)
        self.conn.commit()

    def all_users(self):
        cursor = self.conn.cursor()
        query = """SELECT * FROM users """
        cursor.execute(query)
        rows = cursor.fetchall()
        users = { u[0] : user( u[1], u[2], u[0], u[3] ) for u in rows }
        return users

    def export_to_csv(self, filename):
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter = ';')
            writer.writerow(CSV_HEADERS)

            users = self.all_users()
            for email, user in users.items():
                writer.writerow( [ user.email,
                                   user.name,
                                   user.surname,
                                   user.password ] )
