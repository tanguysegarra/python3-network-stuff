#!/usr/bin/python3

import socket
import sys

def startServer():

    servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 9999
    servSock.bind((host, port))

    servSock.listen(5)
    print("Waiting for a connection...")

    while 42:
        cltSock, addr = servSock.accept()
        print("Got a connection from %s" % str(addr))

        msg = cltSock.recv(1024).decode('ascii')
        
        if msg == "/killserv":
            print("Shutting down server...")
            cltSock.send("Server killed".encode('ascii'))
            sys.exit(0)
        
        print("Received: " + msg)            

        echo = "Thank you for connecting!" + "\n"
        cltSock.send(echo.encode('ascii'))

        cltSock.close()

if __name__ == "__main__":
    startServer()
