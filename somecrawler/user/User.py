__author__ = 'j'
class User:
    username = None
    password = None
    priority = None
    def __init__(self, username, password, priority=5):
        self.username = username
        self.password = password
        self.priority = priority

