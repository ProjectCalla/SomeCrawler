__author__ = 'j'
import threading
import time

class ProducerThread(threading.Thread):

    def run(self):
        print "Starting " + self.name + " time: " + time.time()

