import glob
import json
import os

from . import helpers

search_path=os.getcwd()

# loads matching customers to global variable
def load(term):
    plans = [];
    for fname in glob.iglob(search_path + "/PKG-*.json"):
        with helpers.read_file(fname) as f:
            data = f.readline()
            if term == None or term in data:
                plans.append(json.loads(data))
    return plans

# search plans
def search(term):
    # load matching plans
    return load(term)
