import math
import time
import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT title, url FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Error DataBase')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('''INSERT INTO posts VALUES (NULL, ?, ?, ?)''', (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error DataBase'+str(e))
            return False

        return True

    def addUser(self, name, email, hspw):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM users WHERE email LIKE "{email}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("User already exist with such email")
                return False

            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO users VALUES (NULL, ?, ?, ?, ?)', (name, email, hspw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error'+str(e))
            return False

        return True
