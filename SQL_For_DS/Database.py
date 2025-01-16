import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="sql_practice")
            self.mycursor = self.conn.cursor()
        except:
            print("Connection Error")
            sys.exit(0)
        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO `user_info` (ID, Name, Email, Password) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password))
            self.conn.commit()
            return 1
        except:
            return -1

    def search(self, email, password):
        self.mycursor.execute("""
        SELECT * FROM `user_info` WHERE Email = '{}' AND Password = '{}'
        """.format(email, password))

        data = self.mycursor.fetchall()
        return data

    def get_profile(self, email):
        self.mycursor.execute("""
        SELECT * FROM `user_info` WHERE Email = '{}'
        """.format(email))
        return self.mycursor.fetchone()

    def update_profile(self, name, email, password):
        try:
            self.mycursor.execute("""
            UPDATE `user_info` SET Name = '{}', Email = '{}', Password = '{}' WHERE Email = '{}'
            """.format(name, email, password, email))
            self.conn.commit()
            return 1
        except:
            return -1

    def delete_profile(self, email):
        try:
            self.mycursor.execute("""
            DELETE FROM `user_info` WHERE Email = '{}'
            """.format(email))
            self.conn.commit()
            return 1
        except:
            return -1
