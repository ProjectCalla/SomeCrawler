__author__ = 'j'
from queuelib import pqueue, FifoDiskQueue

class QueueManager:
    qfactory = lambda priority: FifoDiskQueue('queue-dir-%s' % priority)
    pQueue = pqueue.PriorityQueue(qfactory)

    def __init__(self):
        pass
    def createPriorityQueue(self):
        pass
