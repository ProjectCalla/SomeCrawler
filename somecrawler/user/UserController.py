__author__ = 'j'
from somecrawler.user import UserManager
from somecrawler.crawler.manager import MySqlManager
from somecrawler.crawler.config import MySqlConfig as mysqlConf

class UserController:
    u = UserManager.UserManager()
    userList = {}
    mysql = MySqlManager.MySqlManager()
    def __init__(self):
        pass
    def getAllUsers(self):
        users = {}
        query = "SELECT * FROM {0} ;".format(mysqlConf.TABLE_USER)
        db = self.mysql.openDB()
        rows = self.mysql.executeQuery(db, query).fetchall()
        if rows != None:
            i = 0
            for row in rows:
                users[str(i)] = self.u.createUser(row[1], row[2])
                i+=1
        self.mysql.closeDB(db)
        return users