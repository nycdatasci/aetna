#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
   words = line.split()
   print('%d\t1' % len(words[0]))
