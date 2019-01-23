#!/usr/bin/python3

# echo-server: client.py

import socket
import sys

def startClient():
    cltSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
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
    startClient()
