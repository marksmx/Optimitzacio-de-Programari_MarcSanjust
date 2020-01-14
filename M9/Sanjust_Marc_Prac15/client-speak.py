# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = raw_input()
    s.sendto(data, ((HOST,PORT)))
    if(data == 'Bye'):
        break
s.close()
