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
    print(data, filename)
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def print_customers(fields, result, highlights = []):
    row_format = "{:<10}{:<20}: {:<20}"
    for customer in result:
        #print customer name
        print(customer['name']+ ":")
        # filter selected fields
        data = { field: customer[field] for field in fields }
        for field, value in data.items():
            # set highlight
            if field in highlights:
                print('\033[92m')

            print(row_format.format('', field, value))

            # set back to normal
            if field in highlights:
                print('\033[0m')

        print("\n")

