#!/usr/bin/python3

import socket

cltSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
cltSock.connect((host, port))

msg = (input("Send: ")).encode('ascii')
cltSock.send(msg)

echo = cltSock.recv(1024)
print(echo.decode('ascii'))

cltSock.close()
