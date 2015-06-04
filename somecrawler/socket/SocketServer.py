__author__ = 'resul'
from somecrawler.user.User import User
from somecrawler.job.ProducerJob import ProducerJob
from somecrawler.config import Config
import socket
import time
import thread
import Main

class SocketPort:
    def start(self):
        while 1:
            self.open_socket()
            print "Closed Connection...."

    def open_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((Config.SOCKET_HOST, Config.SOCKET_PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            u = conn.recv(1024)
            if not u : break
            a = u.split(',')[0]
            b = u.split(',')[1]
            print eval(a), eval(b)
        conn.close()
        s.close()
