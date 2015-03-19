__author__ = 'j'

import threading
import time
from somecrawler.threads.BaseThread import BaseThread

class ProducerThread(BaseThread):

    def run(self):
        print "Starting " + self.name + " time: " + time.time()

