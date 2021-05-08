#! /usr/bin/python
import argparse

from repositories import phonenumber, helpers

# args parser
parser = argparse.ArgumentParser(description='Process customer list request.', exit_on_error=False, prog='dls')
# supported args
parser.add_argument('field', type=str, nargs='?', choices=phonenumber.fields, help='field to print')
parser.add_argument('--verbose', '-V', help='print more details', action='store_true')
parser.add_argument('--all', '-a', help='print all customers', action='store_true')
parser.add_argument('--show', '-s', nargs='?', help='print customer details', type=str)
parser.add_argument('term', type=str, nargs='?', help='search term eg: 7777777')

# sets printable fields
verbose_fields = {
    'name': ['name', 'address', 'email'],
    'idNumber': ['idNumber', 'name', 'address', 'email'],
    'phoneNumber': ['idNumber', 'name', 'address', 'email', 'staus'],
    'LBPD': ['LBPD', 'unbillCharges', 'outstanding', 'LBAP'],

}

# sets searchable fields
search_rules = { 
    'name': { 'idNumber': True },
    'phoneNumber': { 'idNumber': True, 'phone': False, 'name': True },
    'address': { 'idNumber': True, 'name': True },
    'idNumber': { 'name': True },
}

# print customer details
def print_customers(field, print_fields, search_term):
    result = phonenumber.search_customers(search_term, **search_rules.get(field, {}))

    #print result
    print("Customers:")
    helpers.print_customers(print_fields, result)
    print(str(len(result)) + " matching records(s) found.\n")

# list customers
def list_customers():
    result = phonenumber.search_customers(None)

    #print result
    print("Customers:")
    helpers.list_customers(result)
    print(f"Total {len(result)} customer(s) listed.\n")

def print_customer(term):
    # handle no search term
    if term == None:
        print(f"{helpers.bcolors.WARNING} Provide a phonenumber.")
        return

    result = phonenumber.search_customers(term)

    # handle not found
    if not result:
        print(f"{helpers.bcolors.WARNING} No customer found.")
        return

    print("Customer Details:")
    helpers.print_customer(result[0])


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
    elif args.show :
        # show single customer details
        print_customer(args.show)
    else:
        if args.field == None or args.term == None:
            print(f"{helpers.bcolors.WARNING} Missing arguments.")
            return

        if args.verbose:
            print_fields = verbose_fields.get(args.field, [args.field])
        else:
            print_fields = [args.field]

        print_customers(args.field, print_fields, args.term)
