from socket import *
import threading
import pathlib
import os
import converter
import time
import json 

root = str(os.path.dirname(os.path.abspath(__file__))) + "\\file_systems\\"

serverPort = 5001

start_time = time.time()
interval_time = 1 

serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('', serverPort))

specified_file = input('write root file directory : \n')
print("Your path is defined as " + root + specified_file + "\n")

with open("hostedfile.txt", 'w') as outfile: 
        outfile.write(root + specified_file+"\\")

while 1:
    get_interval = time.time()
    if get_interval - start_time > interval_time:
        
        files = os.listdir(root + specified_file)
        print(files)
        chunklist = []
        for mfile in files:
            if mfile.split(".")[-1] == "png":
                chunklist += converter.divider(root + specified_file+"\\"+mfile, 5)
        json_to_send = {"chunk": chunklist}
        encoded_json = json.dumps(json_to_send).encode('utf-8')
  
        serverSocket.sendto(encoded_json,('localhost',serverPort))
        start_time = get_interval