#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
   words = line.split("\t")
   print('%s\t%s,%s' % (words[16], words[0], float(words[2])/float(words[1])))
