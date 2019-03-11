#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
   word_count = line.split()
   print('%s\t1' % word_count[1])
