import glob
import json
import os

from . import helpers

# holds all customers
customers = [];
fields = ['phoneNumber', 'idNumber', 'name', 'email', 'address', 'staus', 'plan', 'unbillCharges', 'outstanding', 'dataLeft', 'voiceMinLeft', 'LBPD', 'LBAP', 'currNetInUse', 'currCellNetConnected']

# loads matching customers to global variable
def load(term):
    search_path=os.getcwd()
    for fname in glob.iglob(search_path + "/[0-9]*.json"):
        with helpers.read_file(fname) as f:
            data = f.readline()
            if term == None or term in data:
                customers.append(json.loads(data))

# search customers
def search_customers(term):
    # load matching customers
    load(term)
    return customers


