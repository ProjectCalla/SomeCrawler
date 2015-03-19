__author__ = 'j'

from somecrawler.queue import QueueManager, PriorityQueue
from somecrawler.user import User

class SharedMemory:
    #TODO fix this crap
    qManager = QueueManager.QueueManager()
    pQueue = PriorityQueue.PQueue()

def add_item(job):
    SharedMemory.pQueue.put(job, job.priority)

def get_item():
    return SharedMemory.pQueue.get()

def add_itemDEBUG():
    for x in range(0,10):
        SharedMemory.qManager.add_to_queue(SharedMemory.pQueue, User.User(str(x), str(x)), 5)