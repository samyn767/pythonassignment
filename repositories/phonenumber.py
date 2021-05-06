import glob
import json
import os

from . import helpers

search_path=os.getcwd()

# holds all customers
customers = [];
fields = ['phoneNumber', 'idNumber', 'name', 'email', 'address', 'staus', 'plan', 'unbillCharges', 'outstanding', 'dataLeft', 'voiceMinLeft', 'LBPD', 'LBAP', 'currNetInUse', 'currCellNetConnected']

# loads matching customers to global variable
def load(term):
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

def customer_filename(customer):
    return search_path + '/' + str(customer['phoneNumber']) + '.json'

def update(term, fields):
    # load matching customers
    load(term)

    #update customer details
    for customer in customers:
        for field, value in fields.items():
            customer.update({field: value})
            # persist changes
            helpers.write_file(customer, customer_filename(customer))

    return customers

