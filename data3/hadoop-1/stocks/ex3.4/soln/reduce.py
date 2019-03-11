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

for record in getrecords():
   rec = map(lambda x: float(x), record[1])
   decreases = filter(lambda x: x < 0, rec)
   increases = filter(lambda x: x >= 0, rec)
   if decreases == []:
      max_decrease = -1
   else:
      max_decrease = abs(min(decreases))
   if increases == []:
      max_increase = -1
   else:
      max_increase = max(increases)
   print "%s\t%f, %f" % (record[0], max_decrease, max_increase)
