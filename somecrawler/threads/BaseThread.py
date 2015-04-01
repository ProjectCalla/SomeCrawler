__author__ = 'j'

import time, threading
from somecrawler.memory import SharedMemoryManager
from somecrawler.utils import Color
class BaseThread(threading.Thread):
    job = None
    shared_mem = None
    color = None

    def __init__(self, shared_mem, name):
        threading.Thread.__init__(self)
        self.shared_mem = shared_mem
        self.color = Color.get_random_color()
        self.name = name

    def run(self):
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

    def _print(self, message):
        print "{0}{1}: {2}".format(self.color, self.name, message)