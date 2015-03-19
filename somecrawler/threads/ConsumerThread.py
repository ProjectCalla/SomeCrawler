__author__ = 'j'
import threading
import time
from somecrawler.threads.BaseThread import BaseThread
class ConsumerThread(BaseThread):

    def run(self):
        print "Starting Thread. Time: " + time.time()
        # Get lock to synchronize threads
        #threadLock.acquire()

        # Free lock to release next thread
        #threadLock.release()
