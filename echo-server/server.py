#!/usr/bin/python3

# echo-server: server.py

import socket
import sys

def startServer():

    servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 9999
    servSock.bind((host, port))

    servSock.listen(5)

    while 42:
        print("Waiting for a connection...")
        cltSock, addr = servSock.accept()
        print("Got a connection from %s" % str(addr))
        while 42: 
            msg = cltSock.recv(1024).decode('ascii')
        
            if msg == "/killserv":
                print("Shutting down server...")
                cltSock.send("Server killed".encode('ascii'))
                servSock.close()
                sys.exit(0)

            if msg == "/leave":
                print(str(addr) + "disconnected.")
                cltSock.close()
                break
    
            else:
                print("Received: " + msg)            
                echo = "Thank you for your mesage!" + "\n"
                cltSock.send(echo.encode('ascii'))

if __name__ == "__main__":
    startServer()
