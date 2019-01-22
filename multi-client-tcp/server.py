#!/usr/bin/python3

import socket
import _thread as thread
import sys

def cltThread(cltSock, addr):
    msg = cltSock.recv(1024).decode('ascii')
    print("Received from " + str(addr) + " > " + msg)
    echo = "Thank you for connecting!" + "\n"
    cltSock.send(echo.encode('ascii'))
    cltSock.close()

def startServer(port):
    servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    servSock.bind((host, port))

    servSock.listen(5)
    print("Server started!")

    while 42:
        cltSock, addr = servSock.accept()
        print("Got a connection from %s" % str(addr))
        thread.start_new_thread(cltThread, (cltSock, addr))
    
    servSock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./server <PORT>")
    else:
        port = int(sys.argv[1])
        startServer(port)
