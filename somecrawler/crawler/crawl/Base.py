__author__ = 'j'
"""
Interfaces
"""
class BaseProducer():
    def __init__(self):
        pass

    def setup(self):
        """
        Create your connection, do settings etc.
        :return:
        """
        raise Exception("Unimplemented abstract method")

    def start(self):
        """
        Start the Producer.
        :return:
        """
        raise Exception("Unimplemented abstract method")


class BaseConsumer():
    def __init__(self):
        pass

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