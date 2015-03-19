__author__ = 'j'

import time, threading
from somecrawler.memory.SharedMemory import SharedMemory

class BaseThread(threading.Thread):
    job = None
    sharedMem = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.sharedMem = SharedMemory()

    def start(self):
        raise Exception("Unimplemented abstract method: start()")
        #check queue
        #get Job
        #Job.start()
        #done? get new job, repeat

    def thread_infoDEBUG(self):
        name = "BaseThread DEBUG"
        for x in range(100):
            print "{0} -> {1}".format(name, time.time())
            time.sleep(1)

