__author__ = 'j'
from somecrawler.user import User

class UserManager:
    def __init__(self):
        pass
    def createUser(self, username, password):
        return User.User(username, password)
