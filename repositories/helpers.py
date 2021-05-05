from contextlib import contextmanager

@contextmanager
def read_file(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

def print_customers(fields, result):
    row_format = "{:<10}{:<20}: {:<20}"
    for customer in result:
        #print customer name
        print(customer['name']+ ":")
        # filter selected fields
        data = { field: customer[field] for field in fields }
        for field, value in data.items():
            print(row_format.format('', field, value))
        print("\n")

