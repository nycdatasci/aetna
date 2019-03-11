#!/usr/bin/env python
import sys
import string

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

# lis is list of strings "name,average"
def best_hitter(lis):
   return max(lis, key = lambda p: float(p.split(",")[1]))

for record in getrecords():
   print("%s\t%s" % (record[0], best_hitter(record[1].trim())))
