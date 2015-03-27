__author__ = 'j'

from somecrawler.queue import QueueManager, PriorityQueue
from somecrawler.user import User

class SharedMemory(object):
    #TODO fix this crap
    qManager = QueueManager.QueueManager()
    pQueue = PriorityQueue.PQueue()

    def __init__(self):
        pass

    def add_item_to_pQueue(self, job):
        self.pQueue.put(job, job.priority)

    def get_item(self):
        return self.pQueue.get()

    def add_itemDEBUG(self):
        for x in range(0, 10):
            self.qManager.add_to_queue(self.pQueue, User.User(str(x), str(x)), 5)
