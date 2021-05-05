import os
import json


search_path=os.getcwd()+"\\"
for fname in os.listdir(path=search_path):
    
    #print(fname)
    
    data = []
    
    if ".txt" in fname:
        
        with open(fname) as f:
            for line in f:
                data.append(json.loads(line))
                print(data[0]['phoneNumber'])