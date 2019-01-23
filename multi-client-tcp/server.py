#!/usr/bin/python3

# multi-client: server.py

import socket
import _thread as thread
import sys

def cltThread(cltSock, addr):
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
            print("Received from " + str(addr) + " : " + msg)            
            echo = "Thank you for your mesage!" + "\n"
            cltSock.send(echo.encode('ascii'))

def startServer(port):
    servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    servSock.bind((host, port))

    servSock.listen(5)
    print("Server started!")

    while 42:
        cltSock, addr = servSock.accept()
        print("[+] Connection added from %s" % str(addr))
        thread.start_new_thread(cltThread, (cltSock, addr))
    
    servSock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./server <PORT>")
    else:
        port = int(sys.argv[1])
        startServer(port)
