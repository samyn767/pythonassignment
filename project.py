


import argparse
import os
import ast
import json


customer = {
    "phoneNumber" : 7475767,
    "idNumber" : "A074757",
    "name" : "Fathimath Hussian",
    "email" : "faathun@gmail.com",
    "address" : "Veshi, H.Horafushi",
    "staus" : "Active",
    "plan" : "POSTPAID 750",
    "unbillCharges": 750.58,
    "outstanding":250.65,
    "dataLeft" : "8.65 / 15.00 GB",
    "voiceMinLeft" : "25000/30000 MINS",
    "LBPD" : "2nd April 2021",
    "LBAP": "750.23",
    "currNetInUse" : "4G",
    "currCellNetConnected" : "Horafushi Radio Tower"
    
}

if __name__ == '__main__':
    
#write files
    f = open("7475767.txt", "w+")
    f.write(str(customer))
    f.close()
    
    
   #read file 
    print("reading from file .....")
    f = open("7475767.txt", 'r')
    print(f.read())
    
    
    cust={}
    for line in f:
        print("looping start")
        (key, value) = line.strip().split(':')
        cust[key.strip()]=value.strip()
        
        print("key is ", key)
        print("value is", value)
        
    f.close()

        

    