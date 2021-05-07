import argparse
import os
import sys

while 1:
    x = input("Customer Portal Terminal# ")
    if x == "list":
        for x in os.listdir():
            if x.endswith(".json"):
                # Prints only text file names
                file_names = os.path.splitext(x)[0]
                print(file_names)
    

    if x == "exit":
        break


 
    # try:
    #     y = eval(x)
    #     if y: print(y)
    # except:
    #     try:
    #         exec(x)
    #     except Exception as e:
    #         print("error:", e)