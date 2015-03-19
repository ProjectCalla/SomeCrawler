__author__ = 'j'
import time
import threading
class BaseThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

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

