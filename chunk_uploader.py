from socket import *
import json
import os
import math
import datetime

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to upload file')

connectionSocket, addr = serverSocket.accept()

while 1:
    requests = connectionSocket.recv(2048) 
    content_dictionary = json.loads(requests)
    filename = content_dictionary["requested_content"]

    with open("hostedfile.txt", 'r') as infile:
        root = infile.readline()

    root_filename = root + filename
    size = os.path.getsize(root_filename)  
    CHUNK_SIZE = math.ceil(size) 
    with open(root_filename, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
    connectionSocket.send(chunk)
    
    with open('uploadLogs.txt', 'a') as f:  
        f.write(str(datetime.datetime.now()) +" - "+ filename +"\n")

    print("sending successful")
connectionSocket.close()
