__author__ = 'j'
import threading
import time

class Producer(threading.Thread):
    def __init__(self, threadID, name, job, counter, type_thread="Producer"):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.job = job #
        self.type_thread = type_thread

    def run(self):
        print "Starting " + self.name + " time: " + time.time()
        # Get lock to synchronize threads
        #threadLock.acquire()

        # Free lock to release next thread
        #threadLock.release()
