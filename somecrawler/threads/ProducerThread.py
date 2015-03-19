__author__ = 'j'

from somecrawler.memory.SharedMemory import SharedMemory
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
        while 1:
            while 1:
                try:
                    self.job = self.sharedMem.pQueue.get()
                    #Synchronize
                    break
                except:
                    time.sleep(1)
            self.execute_job()

    def execute_job(self):
        print "starting: " + self.job.
        self.job.start()
        print "Done"


    def add_to_shared_memory(self):
        pass