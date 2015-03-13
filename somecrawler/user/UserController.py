__author__ = 'j'
from somecrawler.user import UserManager
from somecrawler.crawler.manager import MySqlManager

class UserController:
    userList = {}
    mysql = MySqlManager.MySqlManager()
    def __init__(self):
        pass
    def getAllUsers(self):
        query = ""
        db = self.mysql.openDB()
        rs = self.mysql.executeQuery(db, query)
        self.mysql.closeDB(db)
