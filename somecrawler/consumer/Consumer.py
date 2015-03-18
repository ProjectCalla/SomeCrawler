__author__ = 'j'
import threading
import time

class Consumer(threading.Thread):
    def __init__(self, threadID, name, job, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.job = job

    def run(self):
        print "Starting " + self.name + " time: " + time.time()
        # Get lock to synchronize threads
        #threadLock.acquire()

        # Free lock to release next thread
        #threadLock.release()
