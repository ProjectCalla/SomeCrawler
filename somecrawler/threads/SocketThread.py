__author__ = 'j'
import threading
from somecrawler.socket import SocketServer
from threading import Thread

class SocketThread(threading.Thread):
    def run(self):
        socket = SocketServer.SocketPort()
        socket.start()

    def __init__(self):
        Thread.__init__(self)


if __name__ == '__main__':
    SocketThread().start()
