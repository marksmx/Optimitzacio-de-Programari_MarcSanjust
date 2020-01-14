# Echo server program
import socket
import time
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50138             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()
conn.sendall("Connect")
time.sleep(1)

while True:
    data = s.recv(1024)
    print >> sys.stderr, data
    if data == 'Bye':
        time.sleep(1)
        break

s.close()
