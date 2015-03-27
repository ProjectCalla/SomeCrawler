__author__ = 'j'
from somecrawler.user import User
from somecrawler.job import JobConfiguration

class UserManager():
    def __init__(self):
        pass
    def createUser(self, username, password, priority=5):
        return User.User(username, password, JobConfiguration.JobConfiguration(), priority)
