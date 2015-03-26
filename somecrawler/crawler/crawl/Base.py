__author__ = 'j'
"""
Interfaces
"""
class BaseProducer():
    def __init__(self):
        pass

    def start(self):
        """
        Start the Producer.
        :return:
        """
        raise Exception("Unimplemented abstract method: start()")

    def package(self, shared_object):
        """
        Package the data and add to Shared Memory
        :return:
        """
        raise Exception("Unimplemented abstract method: package()")


class BaseConsumer():
    source = None
    user = None
    def __init__(self, user, source):
        self.user = user
        self.source = source

    def start(self):
        """
        Start the Consumer.
        :return:
        """
        raise Exception("Unimplemented abstract method")

    def parse(self):
        """
        Start the Consumer.
        :return:
        """
        raise Exception("Unimplemented abstract method")