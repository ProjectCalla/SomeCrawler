__author__ = 'j'
from somecrawler.config import MySqlConfig as mysql_conf
from somecrawler.manager import MySqlManager
from somecrawler.user import UserManager

class UserController():
    u = UserManager.UserManager()
    userList = {}
    mysql = MySqlManager.MySqlManager()
    def __init__(self):
        pass
    def getAllUsers(self):
        users = []
        query = "SELECT * FROM {0}.{1} ;".format(mysql_conf.DATABASE_NAME_DEBUG, mysql_conf.TABLE_USER_DEBUG)
        db = self.mysql.openDB()
        rows = self.mysql.executeQuery(db, query).fetchall()
        if rows is not None:
            i = 0
            for row in rows:
                users.append(self.u.createUser(row[1], row[2]))
                i += 1
        self.mysql.closeDB(db)
        return users