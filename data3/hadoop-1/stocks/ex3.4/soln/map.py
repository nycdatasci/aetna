#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
   record = line.split(",")
   opening = int(record[1])
   closing = int(record[2])
   change = float(closing - opening) / opening
   print '%s\t%s' % (record[0], change)
