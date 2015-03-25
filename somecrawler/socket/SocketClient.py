__author__ = 'resul'
import socket

u = "'0868049', 'passwordd'"
HOST = ''    # The remote host
PORT = 50100              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(u)
data = s.recv(1024)
s.close()