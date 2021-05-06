import glob
import json
import os

from . import helpers

search_path=os.getcwd()

# holds all customers
customers = [];
fields = ['phoneNumber', 'idNumber', 'name', 'email', 'address', 'staus', 'plan', 'unbillCharges', 'outstanding', 'dataLeft', 'voiceMinLeft', 'LBPD', 'LBAP', 'currNetInUse', 'currCellNetConnected']

# loads matching customers to global variable
def load():
    for fname in glob.iglob(search_path + "/[0-9]*.json"):
        with helpers.read_file(fname) as f:
            data = f.readline()
            customers.append(json.loads(data))

# determine if customer matches search query
def match_customer(term, customer, phone = True, idNumber = False, name = False):
    if phone and str(customer['phoneNumber']) == term:
        return True

    if idNumber and customer['idNumber'] == term:
        return True

    if name and term.lower() in customer['name'].lower():
        return True

    return False

# search customers
def search_customers(term, **opts):
    if term == None:
        return customers

    return list(filter(lambda c: match_customer(term, c, **opts), customers))

# get customer filename
def customer_filename(customer):
    return search_path + '/' + str(customer['phoneNumber']) + '.json'

# update customer details
def update(term, fields):
    result = search_customers(term, idNumber = True)
    #update customer details
    for customer in result:
        for field, value in fields.items():
            customer.update({field: value})
            # persist changes
            helpers.write_file(customer, customer_filename(customer))

    return result

# load all customers
load()

