from socket import *
import json


def download_chunk(user, chunk):
    print(user, chunk)
    
    request_content = {"requested content":chunk}
    

with open('files.json') as f:
    lines = f.readlines() 
content_dictionary = json.loads(lines[0])
print(lines)

while 1:
    download_file = input("Type the file which you want to download : ")
    for i in range(1,6):
        searching = True
        searching_chunk = download_file.split(".")[0]+"_"+str(i)
        for user, chunk_list in content_dictionary.items(): # content dict. is like {192.168.2.5 : [chunk_1, chunk_2, chunk_3...]”).
           for chunk in chunk_list: 
               if chunk == searching_chunk:
                    download_chunk(user,chunk)
                    searching = False
        if searching is True:
            print("CHUNK "+searching_chunk+" 3 CANNOT BE DOWNLOADED FROM ONLINE PEERS")

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()