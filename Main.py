__author__ = 'j'
from somecrawler.memory import SharedMemory
from somecrawler.queue import QueueManager

class TestMain:
    queue = QueueManager.QueueManager()
    def __init__(self):
        pass
    def printUser(self, user):
        print user.username
        print user.priority

    def start(self):
        #Create queue
        #add all jobs
        #set producer threads
        #set consumer threads
        #Done


        pass




if __name__ == "__main__":
    TestMain().start()
