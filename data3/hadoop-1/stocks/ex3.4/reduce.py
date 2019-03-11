#!/usr/bin/env python
import sys
import string

def getrecords():
   key, val = sys.stdin.readline().split("\t")
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

for record in getrecords():
   print("%s\t%f" % (record[0], max(map(float, record[1]))))
