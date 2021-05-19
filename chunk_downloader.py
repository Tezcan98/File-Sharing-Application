from socket import *
import json
import converter
import datetime
import converter
serverName = 'localhost'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)  

clientSocket.connect((serverName,serverPort))

def download_chunk(user, chunk): 
    request_content = {"requested_content" : chunk} 
    clientSocket.send(json.dumps(request_content).encode('utf-8'))
    recieved_chunk = clientSocket.recv(65535*64)

    with open("downloaded_files\\"+chunk, 'wb') as infile: 
        infile.write(recieved_chunk)

    with open('downloadLogs.txt', 'w') as f:
        f.write(str(datetime.datetime.now()) +" - "+ chunk + " - "+ user)
    

with open('files.json') as f:
    lines = f.readlines() 
content_dictionary = json.loads(lines[0])
 
 
 
print(lines)

while 1:
    download_file = input("Type the file which you want to download : ")
    success = True
    for i in range(1,6):
        searching = True
        searching_chunk = download_file.split(".")[0]+"_"+str(i)
        for user, chunk_list in content_dictionary.items(): # content dict. is like {192.168.2.5 : [chunk_1, chunk_2, chunk_3...]”).
           for chunk in chunk_list: 
               if chunk == searching_chunk:
                    download_chunk(user,chunk)
                    searching = False
        if searching is True:
            print("CHUNK "+searching_chunk+" CANNOT BE DOWNLOADED FROM ONLINE PEERS")
            success = False
    if success:
        converter.merger("downloaded_files\\"+download_file, 5)

 
clientSocket.close()