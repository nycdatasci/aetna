#!/usr/bin/env python

import sys

for line in sys.stdin:
  nodes = line.strip().split('\t')
  node_from = nodes[0]
  prVal = float(nodes[1])
  node_to = nodes[2:]
  links_len = len(node_to)
  print "%s\t%s" %(node_from, ','.join(node_to))
  if links_len > 0:
    for i in node_to:
      print "%s\t%s" %(i, 1.0 / links_len * prVal)
