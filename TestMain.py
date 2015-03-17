__author__ = 'j'
from somecrawler.memory import SharedMemory
from somecrawler.queue import QueueManager

class TestMain:
    def __init__(self):
        pass
    def printUser(self, user):
        print user.username
        print user.priority

    def start(self):
        #UserController.UserController().getAllUsers()
        pass

    def testSharedMemory(self):
        mem = SharedMemory.SharedMemory

        SharedMemory.addItemDEBUG()
    def testSharedMemory2(self):
        mem = SharedMemory.SharedMemory
        mem.qManager.emptyQueueDEBUG(mem.pQueue)



if __name__ == "__main__":
    #start()
    TestMain().testSharedMemory()
    TestMain().testSharedMemory2()
