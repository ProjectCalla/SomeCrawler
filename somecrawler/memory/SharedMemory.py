__author__ = 'j'
from somecrawler.queue import QueueManager, PriorityQueue
from somecrawler.user import User

class SharedMemory:
    size = 100
    mutex = 0
    qManager = QueueManager.QueueManager()
    pQueue = PriorityQueue.PQueue()

def getItem():
    return SharedMemory.pQueue.get()

def addItemDEBUG():
    for x in range(0,10):
        SharedMemory.qManager.add_to_queue(SharedMemory.pQueue, User.User(str(x), str(x)))