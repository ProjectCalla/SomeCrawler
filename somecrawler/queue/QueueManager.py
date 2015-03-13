__author__ = 'j'
from somecrawler.queue import PriorityQueue
from somecrawler.user import User, UserController
import Queue

class QueueManager:
    pQueue = PriorityQueue.PQueue()
    userCon = UserController.UserController()
    def __init__(self):
        pass
    def add_to_queue(self, user):
        self.pQueue.put(user, user.priority)

    def create_user_priority_queue(self):
        userList = self.userCon.getAllUsers()
        self.add_dict_to_queue(userList)

    def add_dict_to_queue(self, dict):
        for i in range(len(dict)):
            user = dict[str(i)]
            self.pQueue.put(user,user.priority)

    def emptyQueueDEBUG(self):
        while not self.pQueue.empty():
            print self.pQueue.get()