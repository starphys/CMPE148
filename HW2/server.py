# https://docs.python.org/3/library/socket.html#example

#import socket module
from socket import *
import sys # In order to terminate the program


host = ''
port = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
serverSocket.bind((host, port))
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print(f'Ready to serve on {serverSocket.getsockname()} ')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        # Standard OK header, encoded into bytes
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

        #Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

        #Close client socket
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data