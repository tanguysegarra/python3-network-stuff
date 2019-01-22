#!/usr/bin/python3
import socket                                         

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
servSock.bind((host, port))

servSock.listen(5)

while 42:
    cltSock, addr = servSock.accept()
    print("Got a connection from %s" % str(addr))

    msg = cltSock.recv(1024).decode('ascii')
    print("Received: " + msg)

    echo = "Thank you for connecting!" + "\n"
    cltSock.send(echo.encode('ascii'))

    cltSock.close()
