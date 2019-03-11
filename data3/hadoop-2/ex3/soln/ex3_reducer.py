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

def reducer():
    for record in getrecords():
        if len(record[1]) < 20:
            verses = ', '.join(map(lambda x:x.strip(), record[1]))
            print '{0}\t{1}'.format(record[0], verses)

if __name__ == '__main__':
    reducer()
