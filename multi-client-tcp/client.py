#!/usr/bin/python3

# multi-client: client.py

import socket
import sys

def startClient(host, port):
    cltSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    cltSock.connect((host, port))
    while 42:
        msg = input("Send: ")
        enc_msg = msg.encode('ascii')
        if msg == "/leave" or msg == "/killserv":
            cltSock.send(enc_msg)
            cltSock.close()
            sys.exit(0)
        
        cltSock.send(enc_msg)

        echo = cltSock.recv(1024)
        print(echo.decode('ascii'))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./client <IP> <PORT>")
    else:
        host = socket.inet_aton(sys.argv[1]) # modify to make it usable in connect
        port = int(sys.argv[2])
        startClient(host, port)
