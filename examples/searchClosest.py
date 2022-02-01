from fuzzywuzzy import fuzz

from fuzzywuzzy import process

import re


def search_the_closest(query, name_of_file):
    file = open(name_of_file, "r")
    doclist = [line for line in file]
    docstr = ''.join(doclist)
    choices = re.split(r'[;]', docstr)
    x = process.extractOne(query, choices)
    if x[1] > 80:
        return str(x[0])
    else:
        return "Sorry, can You repeat, please?"
