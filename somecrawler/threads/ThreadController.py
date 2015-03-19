__author__ = 'j'
import ConsumerThread, ProducerThread
class ThreadController():
    consumer_threads = []
    producer_threads = []

    def __init__(self):
        pass
    def spawn_consumer_threads(self, amount):
        for i in range(amount):
            self.consumer_threads.append(ConsumerThread.ConsumerThread())

    def spawn_producer_threads(self, amount):
        for i in range(amount):
            self.producer_threads.append(ProducerThread.ProducerThread())
