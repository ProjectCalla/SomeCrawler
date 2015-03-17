__author__ = 'j'

from somecrawler.config import MySqlConfig
import MySQLdb
from time import strftime
import logging

class MySqlManager():
    def __init__(self):
        pass
    def openDB(self):
        logging.info("Creating Database Connection.")
        db = MySQLdb.connect(host= MySqlConfig.CONNECTION_URL,
                      user= MySqlConfig.CONNECTION_USERNAME, # your username
                      passwd= MySqlConfig.CONNECTION_PASSWORD, # your password
                      db= MySqlConfig.DATABASE_NAME) # name of the data base
        return db
    def closeDB(self, db):
        logging.info("Closing Database Connection.")
        db.close()

    def executeQuery(self, db, query):
        logging.info("Executing Query.")
        cur = db.cursor()
        cur.execute(query)
        return cur
    def getTimestamp(self):
        return strftime("%Y-%m-%d %H:%M:%S")
