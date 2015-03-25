__author__ = 'j'

from somecrawler.memory import SharedMemoryManager
import threading, time
from somecrawler.threads.BaseThread import BaseThread

class ProducerThread(BaseThread):

    def run(self):
        #check if done
        #done? pull new job out of queue
        #start job
        print "Starting thread"
        self.initialize()

    def initialize(self):
        index = 0
        while 1:
            if index == 10:
                break
            while 1:
                try:
                    if self.shared_mem.pQueue.counter != 0:
                        self.job = self.shared_mem.pQueue.get()
                        #Synchronize
                        break
                    else:
                        int("goto except")
                except:
                    print "[PRODUCER_THREAD] self.sharedMem.pQueue.counter = %s" % self.shared_mem.pQueue.counter
                    if index == 10:
                        print index
                        break
                    time.sleep(1)

                    index += 1
            if self.job != None:
                self.execute_job()
        print "Donejob"

    def execute_job(self):
        #lock_object = self.l
        self.job.start()
        print "Done"


    def add_to_shared_memory(self):
        pass