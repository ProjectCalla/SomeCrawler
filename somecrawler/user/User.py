__author__ = 'j'

class User():
    username = None
    password = None
    priority = None
    job_configuration = None

    def __init__(self, username, password, job_configuration, priority=5):
        self.username = username
        self.password = password
        self.job_configuration = job_configuration
        self.priority = priority

