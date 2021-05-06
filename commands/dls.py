#! /usr/bin/python
import argparse

from repositories import phonenumber, helpers

def list_customers(fields, search_term):
    if fields == None:
        print('No fields selected. use -V to print all fields.')

    result = phonenumber.search_customers(search_term)

    #print result
    print("Customers:")
    helpers.print_customers(fields, result)
    print(str(len(result)) + " matching result(s) found.")

# process request
def execute():
    parser = argparse.ArgumentParser(description='Process customer list request.')
    parser.add_argument('field', type=str, nargs='?', help='field to print: ' + (', ').join(phonenumber.fields))
    parser.add_argument('--verbose', '-V', help='print all fields', action='store_true')
    parser.add_argument('term', type=str, nargs='?', help='search term eg: 7777777')

    args = parser.parse_args()
    print(args)

    field = phonenumber.fields if args.verbose else [args.field]
    term = args.field if args.verbose else args.term

    list_customers(field, term)
