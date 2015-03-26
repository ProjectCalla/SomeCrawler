__author__ = 'resul'
import socket
from somecrawler.config import Config

u = "'0868049', 'Yalihuyuk42'"

class Client:
    def start(self):
        self.client_connect()

    def client_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((Config.SOCKET_HOST, Config.SOCKET_PORT))
        s.sendall(u)
       # data = s.recv(1024)

Client().start()