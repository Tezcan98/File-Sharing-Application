from socket import *
import json

serverIP = '25.90.43.255'
serverPort = 5001
server_address = (serverIP, serverPort)

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(server_address) 
 
with open("files.json","w") as f: ## dosya yoksa olustur varsa sıfırla
    f.write("") 
while 1:
    message, server = clientSocket.recvfrom(8096) 
    json_string = message.decode("utf-8") 

    content_dictionary_string = json_string.replace('chunk',server[0])

    print(content_dictionary_string)
    content_dictionary = json.loads(content_dictionary_string)
    

    line = ""
    with open("files.json","r") as f:
        line = f.readlines() 
    with open('files.json', 'w') as f: 
        if len(line) > 0: 
            line = line[0]
            line = line.replace("'", '"')
            file_content = json.loads(line) 
            file_content[server[0]] = content_dictionary[server[0]] 
            f.write(str(file_content)) 

        else:
            f.write(content_dictionary_string)
clientSocket.close()