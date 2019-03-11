#!/usr/bin/env python

import sys
import string

def getrecords():
    key, val = sys.stdin.readline().split("\t")
    vals = [val.strip()]
    while True:
 	if key == None:
 	    return
	line = sys.stdin.readline()
	if line == "":
	    returnval = (key, vals)
	    key = None
	    yield returnval
	else:
	    newkey, val = line.split("\t")
	    if newkey == key:
		vals = vals + [val.strip()]
 		continue
 	    else:
 		returnval = (key, vals)
 		key = newkey
 		vals = [val.strip()]
 		yield returnval

for record in getrecords():
    print("%s\t%s" % (record[0], '\t'.join(record[1])))
