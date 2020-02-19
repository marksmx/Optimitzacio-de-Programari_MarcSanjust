# Echo client program
import socket
import sys
import threading

HOST = 'localhost'    # The remote host
PORT = 51130           # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
print 'CONEX2'

def send(mess1):
    while True:
        data1 = raw_input()
        mess1.sendall(data1)

        if data1 == "Bye":
            break

def rec(s):
    while True:
        t=s.recv(1024)
        print t

        if t == "Bye":
            s.sendall(data1)
            break



dae1 = threading.Thread(target = send, args=(s,))
dae1.daemon=True
dae1.start()

dae2 = threading.Thread(target = rec, args = (s,))
dae2.start()
dae2.join()

s.close()
