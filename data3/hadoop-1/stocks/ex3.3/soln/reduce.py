#!/usr/bin/env python
import sys
import string

def getrecords():
   key, val = sys.stdin.readline().split()
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
        (newkey, val) = line.split()
        if newkey == key:
           vals = vals + [val]
           continue
        else:
           returnval = (key, vals)
           key = newkey
           vals = [val]
           yield returnval

for record in getrecords():
   print(record[0], max(map(lambda x: float(x), record[1])))
