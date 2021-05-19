from socket import *
import json
import os
import math

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()

while 1:
    requests = connectionSocket.recv(2048)

    content_dictionary = json.loads(requests)
    filename = content_dictionary["requested_content"]

    with open("hostedfile.txt", 'r') as infile:
        root = infile.readline()

    filename = root + filename
    size = os.path.getsize(filename)  
    CHUNK_SIZE = math.ceil(size) 
    with open(filename, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
    connectionSocket.send(chunk)

    print("sending successful")
connectionSocket.close()
