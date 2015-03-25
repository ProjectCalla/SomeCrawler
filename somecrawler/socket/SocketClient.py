__author__ = 'resul'
import socket
from somecrawler.config import Config

u = "'0868049', 'passwordd'"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Config.SOCKET_HOST, Config.SOCKET_PORT))
s.sendall(u)
data = s.recv(1024)
s.close()