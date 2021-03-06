__author__ = 'j'
from Queue import PriorityQueue

class PQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        if self.counter > 0:
            _, _, item = PriorityQueue.get(self, *args, **kwargs)
            self.counter -= 1
            return item
        else:
            return None