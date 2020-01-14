# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 50138              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
t=s.recv(1024)
print t

while True:
    data = raw_input()
    s.sendto(data, ((HOST,PORT)))
    if(data == 'Bye'):
        break

s.close()
