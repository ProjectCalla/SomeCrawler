__author__ = 'j'

from somecrawler.memory import SharedMemoryManager
import threading, time
from somecrawler.threads.BaseThread import BaseThread
from somecrawler.config import Config

class ConsumerThread(BaseThread):

    def run(self):
        #check if done
        #done? pull new job out of queue
        #start job
        print "Starting thread"
        self.initialize()

    def initialize(self):
        index = 0
        while 1:
            self.get_job()
            self.execute_job()
        print "Donejob"

    def execute_job(self):
        #lock_object = self.l
        self.job.start()
        print "Done"

    def get_job(self):
        i = 0
        while 1:
            if self.shared_mem.pQueue.counter != 0:
                self.job = self.shared_mem.pQueue.get()
                return
            else:
                time.sleep(1)
                i += 1
                if i >= Config.timeout:
                    print "Stop thread, but how?"