#!/usr/bin/env python

import sys
import re


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
  key = record[0]
  outlinks = list(filter(lambda x: x[0].isalpha(), record[1]))
  outlinks = outlinks[0].strip().split(',')
  vals = list(filter(lambda x: not x[0].isalpha(), record[1]))
  val = sum(map(float, vals))
  print("%s\t%s\t%s" %(key, str(val), '\t'.join(outlinks)))
