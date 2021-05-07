#! /usr/bin/python
import argparse

from repositories import phonenumber, helpers

# args parser
parser = argparse.ArgumentParser(description='Process customer list request.', exit_on_error=False, prog='dls')
# supported args
parser.add_argument('field', type=str, nargs='?', choices=phonenumber.fields, help='field to print')
parser.add_argument('--verbose', '-V', help='print more details', action='store_true')
parser.add_argument('--all', '-a', help='print all customers', action='store_true')
parser.add_argument('term', type=str, nargs='?', help='search term eg: 7777777')

# sets printable fields
verbose_fields = {
    'name': ['name', 'address', 'email'],
    'idNumber': ['idNumber', 'name', 'address', 'email'],
    'phoneNumber': ['idNumber', 'name', 'address', 'email', 'staus'],
    'LBPD': ['LBPD', 'unbillCharges', 'outstanding', 'LBAP'],

}

# sets searchable fields
search_args = { 
    'name': { 'idNumber': True },
    'phoneNumber': { 'idNumber': True, 'phone': False, 'name': True },
    'address': { 'idNumber': True, 'name': True },
    'idNumber': { 'name': True },
}

# list customers
def print_customers(field, print_fields, search_term):
    result = phonenumber.search_customers(search_term, **search_args.get(field, {}))

    #print result
    print("Customers:")
    helpers.print_customers(print_fields, result)
    print(str(len(result)) + " matching records(s) found.\n")

def list_customers():
    result = phonenumber.search_customers(None)

    #print result
    print("Customers:")
    helpers.list_customers(result)
    print(f"Total {len(result)} customer(s) listed.\n")

# process request
def execute(input):
    try:
        args = parser.parse_args(input)
    except argparse.ArgumentError:
        print(f"{helpers.bcolors.WARNING}Invalid Arguments{helpers.bcolors.ENDC}")
        return
    except SystemExit:
        return

    # print all customers
    if args.all:
        list_customers()
    else:
        if args.field == None:
            print(f"{helpers.bcolors.WARNING} No field selected.")
            return

        if args.verbose:
            print_fields = verbose_fields.get(args.field, [args.field])
        else:
            print_fields = [args.field]

        print_customers(args.field, print_fields, args.term)
