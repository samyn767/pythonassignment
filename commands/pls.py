#! /usr/bin/python
import argparse

from repositories import mobile_plan, helpers

# args parser
parser = argparse.ArgumentParser(description='Process plan list request.', exit_on_error=False, prog='pls')
# supported args
parser.add_argument('term', type=str, nargs='?', help='search term eg: "POSTPAID 700"')
parser.add_argument('--show', '-s', help='print all plan details', action='store_true')

def list_plans(term):
    result = mobile_plan.search(term)

    #print result
    print("Plans:")
    helpers.list_plans(result)
    print(f"Total {len(result)} plans(s) listed.\n")

def show_plans(term):
    result = mobile_plan.search(term)

    #print result
    print("Plans:")
    helpers.print_plans(result)
    print(f"Total {len(result)} plans(s) listed.\n")

# process request
def execute(input):
    try:
        args = parser.parse_args(input)
    except argparse.ArgumentError:
        print(f"{helpers.bcolors.WARNING}Invalid Arguments{helpers.bcolors.ENDC}")
        return
    except SystemExit:
        return

    if args.show:
        show_plans(args.term)
    else:
        list_plans(args.term)
