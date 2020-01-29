# Echo client program
import socket
import sys
import threading

HOST = 'localhost'    # The remote host
PORT = 50137           # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send(mess):
    while True:
        data = raw_input()
        mess.sendall(data)

        if data == "Bye":
            break

def rec(s):
    while True:
        t=s.recv(1024)
        print t

        if t == "Bye":
            s.sendall(data)
            break



dae1 = threading.Thread(target = send, args=(s,))
dae1.daemon=True
dae1.start()

dae2 = threading.Thread(target = rec, args = (s,))
dae2.start()
dae2.join()

s.close()
