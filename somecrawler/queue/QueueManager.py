__author__ = 'j'
from somecrawler.queue import PriorityQueue
from somecrawler.user import User, UserController

class QueueManager:
    #pQueue = PriorityQueue.PQueue()
    userCon = UserController.UserController()

    def __init__(self):
        pass
    def add_to_queue(self, pQueue, user):
        pQueue.put(user, user.priority)

    def create_user_priority_queue(self, pQueue):
        userList = self.userCon.getAllUsers()
        self.add_dict_to_queue(userList, pQueue)

    def add_dict_to_queue(self, pQueue, dict):
        for i in range(len(dict)):
            user = dict[str(i)]
            pQueue.put(user, user.priority)
        return pQueue

    def emptyQueueDEBUG(self, pQueue):
        i = 0
        while not pQueue.empty():
            print i, pQueue.get()
            i += 1