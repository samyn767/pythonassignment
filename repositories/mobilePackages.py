import glob
import json
import os

from . import helpers

search_path=os.getcwd()

# holds all plans
mPackage = [];
fields = ['name', 'data', 'freemin', 'email', 'sms', 'freeSocial', 'freeapps', 'price', 'intd', 'excharge']

# loads matching customers to global variable
def load(term):
    for fname in glob.iglob(search_path + "/(PKG-)*.json"):
        with helpers.read_file(fname) as f:
            data = f.readline()
            if term == None or term in data:
                mPackage.append(json.loads(data))

# search customers
def search_plans(term):
    # load matching plans
    load(term)
    return mPackage

def plans_filename(mPackage):
    return search_path + '/' + str(mPackage['name']) + '.json'

def update(term, fields):
    # load matching plans
    load(term)

    #update customer details
    for mPackage in mPackages:
        for field, value in fields.items():
            mPackage.update({field: value})
            # persist changes
            helpers.write_file(mPackage, plans_filename(mPackage))

    return mPackage

