__author__ = 'j'
from somecrawler.queue import PriorityQueue
from somecrawler.user import User, UserController

class QueueManager:
    pQueue = PriorityQueue.PQueue()
    userCon = UserController.UserController()

    def __init__(self):
        pass

    def add_to_queue(self, pQueue, job, priority):
        pQueue.put(job, priority)

    def create_user_priority_queue(self, pQueue):
        userList = self.userCon.getAllUsers()
        self.add_dict_to_queue(userList, pQueue)

    def add_dict_to_queue(self, pQueue, dict):
        for i in range(len(dict)):
            job = dict[str(i)]
            pQueue.put(job, job.priority)
        return pQueue

    def emptyQueueDEBUG(self, pQueue):
        i = 0
        while not pQueue.empty():
            print i, pQueue.get()
            i += 1