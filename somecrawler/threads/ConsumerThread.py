__author__ = 'j'
import threading
import time
from somecrawler.threads.BaseThread import BaseThread
class ConsumerThread(BaseThread):

    def run(self):
        #check if done
        #done? pull new job out of queue
        #start job
        print "[CONSUMER_THREAD] Starting thread"
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
                    print "[CONSUMER_THREAD] Thread sleeping {0}/{1}".format(index, 10)
                    if index == 10:
                        print index
                        break
                    time.sleep(5)
                    index += 1

            if self.job != None:
                self.execute_job()
        print "[CONSUMER_THREAD] Thread Done"

    def execute_job(self):
        #lock_object = self.l
        self.job.start()
        print "Done"
