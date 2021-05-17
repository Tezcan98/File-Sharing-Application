import os
import math 

def divider(filename, piece):  
    content_name = filename.split('.')[0]
    c = os.path.getsize(filename) 
    
    chunk_list = []
    CHUNK_SIZE = math.ceil(math.ceil(c)/ piece)   
    index = 1
    with open(filename, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
        while chunk:
            chunkname = content_name+'_'+str(index) 
            chunk_list.append(chunkname.split("\\")[-1])
            with open(chunkname,'wb+') as chunk_file:
                chunk_file.write(chunk)
            index += 1
            chunk = infile.read(int(CHUNK_SIZE))
    chunk_file.close()
    
    return chunk_list
 

def merger(filename, piece):  
    content_name = filename.split('.')[0]
    chunknames = []
    for i in range(1,piece):
        chunknames.append(content_name+"_"+i) 
    
    with open(filename, 'wb') as outfile: 
        for chunk in chunknames: 
            with open(chunk, 'rb') as infile: 
                outfile.write(infile.read() )
            infile.close() 
