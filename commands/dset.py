#! /usr/bin/python
import argparse

from repositories import phonenumber, mobile_plan, helpers

def update_customers(fields, search_term):
    result = phonenumber.update(search_term, fields)

    #print result
    if len(result):
        print("Following " + str(len(result)) + " record(s) updated successfully.")
        helpers.print_customers(phonenumber.fields, result, fields.keys())
        print("\n")
    else:
        print("No matching records found.\n")

# get all plans
plans = mobile_plan.load(None)
# args parser
parser = argparse.ArgumentParser(description='Update customer details.', prog='dset')
# supported args
parser.add_argument('--id', nargs='?', help='update ID card number.')
parser.add_argument('--name', nargs='?', help='update customer name.')
parser.add_argument('--email', nargs='?', help='update customer email.')
parser.add_argument('--address', nargs='?', help='update customer address.')
parser.add_argument('--staus', nargs='?', choices = ['Active', 'Barred', 'Terminated'], help='update customer status.')
parser.add_argument('--plan', nargs='?', choices= [p['name'] for p in plans], help='update customer plan.')
parser.add_argument('term', help='search term eg: 7777777')

# process request
def execute(input):
    try:
        args = parser.parse_args(input)
    except argparse.ArgumentError:
        print("Invalid Arguments")
        return
    except SystemExit:
        return

    fields = dict(filter(lambda f: f[0] != 'term' and f[1] != None, vars(args).items()))

    if 'id' in fields:
        fields['idNumber'] = fields.pop('id')

    update_customers(fields, args.term)

