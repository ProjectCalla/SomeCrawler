__author__ = 'j'
import threading, time
class SomeThread():
    def __init__(self, name):
        self.threading = threading
        self.t = self.threading.Thread(target=self.foo, args=name).start()
    def foo(self, name):
        for x in range(100):
            print "{0} -> {1}".format(name, time.time())
            time.sleep(1)
            print "[Thread info {0}] {1} :: {2}".format(name, "active count", self.threading.active_count())
            print "[Thread info {0}] {1} :: {2}".format(name, "current thread", self.threading.current_thread())
