__author__ = 'j'

import MySQLdb
from somecrawler.crawler.config import MySqlConfig
import datetime
from time import strftime

class MySqlManager:
    def __init__(self):
        pass
    def openDB(self):
        db = MySQLdb.connect(host= MySqlConfig.CONNECTION_URL,
                      user= MySqlConfig.CONNECTION_USERNAME, # your username
                      passwd= MySqlConfig.CONNECTION_PASSWORD, # your password
                      db= MySqlConfig.DATABASE_NAME) # name of the data base
        return db
    def closeDB(self, db):
        db.close()

    def executeQuery(self, db, query):
        return db.cursor().execute(query)

    def getTimestamp(self):
        return strftime("%Y-%m-%d %H:%M:%S")
