__author__ = 'resul'
from somecrawler.user.User import User
from somecrawler.job.ProducerJob import ProducerJob
import socket
import Queue, time
import Main

class SocketPort:
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50100              # Arbitrary non-privileged port
    def start(self):
        while 1:
            self.open_socket()
            print "Closed Connection...."

    def open_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST, self.PORT))
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            u = conn.recv(1024)
            if not u : break
            a = u.split(',')[0]
            b = u.split(',')[1]
            print eval(a), eval(b)
            #q.put(data)
            #for a in range(q.qsize()):
             #   print q.get()
                #time.sleep(2)
        conn.close()

        user = User(a, b, 7)
        ProducerJob(user, osiris_personalia=True)
SocketPort().start()