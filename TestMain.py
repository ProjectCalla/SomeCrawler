__author__ = 'j'
from somecrawler.user import UserController, UserManager, User
from somecrawler.queue import QueueManager

queueMan = QueueManager.QueueManager()

def printUser(user):
    print user.username
    print user.priority

def start():
    #UserController.UserController().getAllUsers()
    queueMan.create_user_priority_queue()




if __name__ == "__main__":
    start()