#! /usr/bin/python
import argparse

from repositories import phonenumber, helpers

# args parser
parser = argparse.ArgumentParser(description='Process customer list request.', exit_on_error=False, prog='dls')
# supported args
parser.add_argument('field', type=str, choices=phonenumber.fields, help='field to print')
parser.add_argument('--verbose', '-V', help='print more details', action='store_true')
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
def list_customers(field, print_fields, search_term):
    result = phonenumber.search_customers(search_term, **search_args.get(field, {}))

    #print result
    print("Customers:")
    helpers.print_customers(print_fields, result)
    print(str(len(result)) + " matching records(s) found.")

# process request
def execute(input):
    try:
        args = parser.parse_args(input)
    except argparse.ArgumentError:
        print("Invalid Arguments")
        return
    except SystemExit:
        return

    if args.verbose:
        print_fields = verbose_fields.get(args.field, [args.field])
    else:
        print_fields = [args.field]

    list_customers(args.field, print_fields, args.term)
