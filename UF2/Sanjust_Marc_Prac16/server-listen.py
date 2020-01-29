# Echo server program
import socket
import time
import sys
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50137             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()

def send(conn):
    while True:
        text_env = raw_input()
        conn.sendall(text_env)

        if text_env == "Bye":
            break

def rec(data):
    while True:
        data = conn.recv(1024)
        print data

        if data == "Bye":
            break

dae1 = threading.Thread(target = send, args = (conn,))
dae1.daemon=True
dae1.start()

dae2 = threading.Thread(target = rec, args = (conn,))
dae2.start()
dae2.join()

s.close()
