#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
   words = line.split()
   for word in words:
      print('%s\t1' % word)
