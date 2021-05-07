
import argparse
import os
import json


def seachunknown(data,output):
    #print(data)
    search_path=os.getcwd()+"\\"
    cust=[]
    for fname in os.listdir(path=search_path):
        if fname.endswith(".txt"):
            fo = open(search_path + fname)
            line = fo.readline()
            line_no = 1
            while line != '' :
                index = line.find(data)
                if ( index != -1) :
                    with open(fname) as f:
                         for line in f:
                              cust.append(json.loads(line))
                    #print("Cutomer Number",cust[0]['phoneNumber'])
                    #return (cust[0]['phoneNumber'])
                
                
                else:
                    break
                line = fo.readline()
                line_no += 1
            fo.close
    if output ==1:
        print(cust[0]['name']+" ", cust[0]['phoneNumber'])

def nameSearch(data,output):
    seachunknown(data,output)
    

def findAllCust(para):
    data = []
    search_path=os.getcwd()+"\\"
    if para == "all":
         for fname in os.listdir(path=search_path):
    
              if ".txt" in fname:
        
                  with open(fname) as f:
                    for line in f:
                     data.append(json.loads(line))
                     print(data[0]['phoneNumber'])
                
                

            
            
parser = argparse.ArgumentParser(description='SIMPLE EXAMPLE')


parser.add_argument('-s', '--search', help='search customer using any parameter')
parser.add_argument('-f', '--find', help='list all customers')
parser.add_argument( 'NAME', help='list all customers')
parser.add_argument( 'EXIT', help='exit program')


while 1:
    args = parser.parse_args(input("Dhiraagu #: ").split())
    #print (args)
    
    if args.search !=None and args.NAME =="name":
        print(args)
        seachunknown(args.search,1)
    #filename= seachunknown(args.find)
    #print(filename)
    elif args.find:
        findAllCust(args.find)
    elif args.search !=null and args.NAME ==null:
        seachunknown(args.search,1)
    elif args.exit =="exit":
        break
