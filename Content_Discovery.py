from socket import *
import json

serverIP = 'localhost'
serverPort = 5001
server_address = (serverIP, serverPort)

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(server_address) 
 


modifiedMessage, server = clientSocket.recvfrom(65536) 
json_string = modifiedMessage.decode("utf-8")
print(server) 

content_dictionary_string = json_string.replace('chunk\"',server[0]+'\"')

content_dictionary = json.loads(content_dictionary_string)
# TODO: WILL SHARE WITH DOWNLOAD PROCCESS 
with open('files.json', 'w') as f:
    f.write(content_dictionary_string)

clientSocket.close()