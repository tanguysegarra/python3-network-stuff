#!/usr/bin/python3

import socket
import sys

def startClient(host, port):
    cltSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    cltSock.connect((host, port))

    msg = (input("Send: ")).encode('ascii')
    cltSock.send(msg)

    echo = cltSock.recv(1024)
    print(echo.decode('ascii'))

    cltSock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./client <IP> <PORT>")
    else:
        host = socket.inet_aton(sys.argv[1])
        port = int(sys.argv[2])
        startClient(host, port)
