#!/usr/bin/env python

import sys

def getrecords():
   (key, val) = sys.stdin.readline().split("\t");
   vals = [val]
   while True:
      if key == None:
         return
      line = sys.stdin.readline()
      if line == "":
         returnval = (key, vals)
         key = None
         yield returnval
      else:
        (newkey, val) = line.split("\t")
        if newkey == key:
           vals = vals + [val]
           continue
        else:
           returnval = (key, vals)
           key = newkey
           vals = [val]
           yield returnval

def combiner():
    for record in getrecords():
        # your code goes here
        print('{0}\t{1} {2} {3} {4}'.format(record[0],min(v),max(v),sum(v),len(v)))

if __name__ == '__main__':
    combiner()
