import json
from contextlib import contextmanager

@contextmanager
def read_file(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

def write_file(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def print_customers(fields, result, highlights = []):
    row_format = "{:<10}{:<20}: {:<20}"
    for customer in result:
        #print customer name
        print(f"{bcolors.OKGREEN}\t{customer['name'].upper()}{bcolors.ENDC}")
        # filter selected fields
        data = { field: customer[field] for field in fields }
        for field, value in data.items():
            # set highlight
            if field in highlights:
                print(bcolors.OKBLUE + row_format.format('', field, value) + bcolors.ENDC)
            else:
                print(bcolors.OKCYAN + row_format.format('', field, value) + bcolors.ENDC)

        print("\n")

def list_customers(customers):
    row_format = "\t{:<12} {:<10} {:<20} {:<10}"
    #print header
    print(bcolors.OKGREEN + bcolors.BOLD + row_format.format("PHONE", "ID NUMBER", "CUSTOMER NAME", "STATUS") + bcolors.ENDC)
    for customer in customers:
        print(bcolors.OKCYAN + row_format.format(customer['phoneNumber'], customer['idNumber'], customer['name'], customer['staus']) + bcolors.ENDC)

def list_plans(plans):
    row_format = "\t{:<5} {:<20} {:<10}"
    #print header
    print(bcolors.OKGREEN + bcolors.BOLD + row_format.format("", "PLAN NAME", "PRICE") + bcolors.ENDC)
    for index, plan in enumerate(plans, start=1):
        print(bcolors.OKCYAN + row_format.format(index, plan['name'], plan['price']) + bcolors.ENDC)

def print_plans(plans):
    row_format = "{:<10}{:<20}: {:<20}"

    for plan in plans:
        #print customer name
        print(f"{bcolors.OKGREEN}\t{plan['name'].upper()}{bcolors.ENDC}")
        # filter selected fields
        for field, value in plan.items():
            print(bcolors.OKCYAN + row_format.format('', field, value) + bcolors.ENDC)

        print("\n")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

