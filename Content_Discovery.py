from socket import *
import json

serverIP = 'localhost'
serverPort = 5001
server_address = (serverIP, serverPort)

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(server_address) 
 

while 1:
    message, server = clientSocket.recvfrom(8096) 
    json_string = message.decode("utf-8")
    print(server, json_string) 

    content_dictionary_string = json_string.replace('chunk',server[0])

    content_dictionary = json.loads(content_dictionary_string)
    # TODO: WILL SHARE WITH DOWNLOAD PROCCESS 
    with open('files.json', 'w') as f:
        f.write(content_dictionary_string)

clientSocket.close()