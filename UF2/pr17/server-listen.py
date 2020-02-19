# Echo server program
import socket
import time
import sys
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 51133             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
l = []
print 'CONEX'

def rec():
    while True:
        conn, addr = s.accept()
        l.append(conn)
        dae3 = threading.Thread(target = echo, args = (conn,))
        dae3.start()


def echo(conn):
    while True:
        data = conn.recv(1024)

        for x in l:
            if x != conn:
                x.sendall(data)

        if (data == "Bye" or data == "Bye\n"):
            l.remove(x)
            x.close()
            break

dae2 = threading.Thread(target = rec)
dae2.start()
dae2.join()

s.close()
