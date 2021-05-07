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

