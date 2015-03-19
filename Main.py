__author__ = 'j'
from somecrawler.memory import SharedMemory
from somecrawler.queue import QueueManager
from somecrawler.job import ConsumerJob, ProducerJob
from somecrawler.user import User
import thread
from somecrawler.exp import SomeThread
from somecrawler.threads import BaseThread
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
    def test(self):
        a = BaseThread.BaseThread()
        a.start()


if __name__ == "__main__":
    #TestMain().start()
    TestMain().test()
    #TestMain().test2()