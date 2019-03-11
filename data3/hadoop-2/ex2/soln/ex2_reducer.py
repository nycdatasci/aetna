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

def reducer():
    for record in getrecords():
        vals = map(lambda x: x.split(), record[1])
        v1, v2, v3, v4 = reduce(lambda x,y:[float(a)+float(b) for a,b in zip(x,y)], vals)
        mean = float(v3) / float(v4)
        print '{0}\t{1} {2} {3} {4} {5}'.format(record[0], v1, v2, v3, v4, mean)

if __name__ == '__main__':
    reducer()
