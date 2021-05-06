#! /usr/bin/python
import argparse

from repositories import phonenumber, helpers

# list customers
def list_customers(fields, search_term):
    if fields == None:
        print('No fields selected. use -V to print all fields.')

    result = phonenumber.search_customers(search_term)

    #print result
    print("Customers:")
    helpers.print_customers(fields, result)
    print(str(len(result)) + " matching result(s) found.")

# args parser
parser = argparse.ArgumentParser(description='Process customer list request.', exit_on_error = False, prog='dls')
# supported args
parser.add_argument('field', type=str, choices=phonenumber.fields, help='field to print')
parser.add_argument('--verbose', '-V', help='print all fields', action='store_true')
parser.add_argument('term', type=str, nargs='?', help='search term eg: 7777777')

# process request
def execute(input):
    try:
        args = parser.parse_args(input)
    except argparse.ArgumentError:
        print("Invalid Arguments")
        return
    except SystemExit:
        return

    field = phonenumber.fields if args.verbose else [args.field]

    list_customers(field, args.term)
