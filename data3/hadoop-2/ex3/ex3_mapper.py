#! /usr/bin/env python

import sys
import re

# cleaner() replace everything except letters and ' with white space
def cleaner(line): 
    return re.sub(r'[^a-zA-Z\s\']', ' ', line).strip().lower()

def mapper():

    for record in sys.stdin:
        try:
            # your code goes here
        except:
            pass


if __name__ == '__main__':
    mapper()
