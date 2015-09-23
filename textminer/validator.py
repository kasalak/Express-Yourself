import re


def binary(string):
    return re.match(r'[01]', string)

def binary_even(string):
    return re.match(r'[01]+[^1]$', string)

def hex(string):
    return re.match(r'\b[A-Fa-f0-9]+$', string)

def word(string):
    return re.match(r'(^[0-9a-z-]*[a-z]$)', string)

def words(string, count=None):
    split_string = re.split(" ", string)
    if count:
        if count != len(split_string):
            return False
    if None in [re.match(r'(^[0-9a-z-]*[a-z]$)', string) for string in split_string]:
        return False
    else:
        return True

def phone_number(string):
    return re.match(r'\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})', string)

def money(string):
    return re.match(r'^\$\d{1,3}([,]?\d{3})*([.]\d{2})?$', string)

def zipcode(string):
    return re.match(r'^\d{5}?(-?\d{4})?$', string)

def date(string):
    return re.match(r'^\d{1,4}[-/]\d{1,2}[-/]?\d{2,4}?$', string)
                
