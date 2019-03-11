#!/usr/bin/env python
import sys

for line in sys.stdin:
	nodes = line.strip().split('\t')
 	node_from = nodes[0]
 	node_to = nodes[1:]
 	links_len = len(node_to)
 	if links_len > 0:
 		for i in node_to:
 			print "%s\t%s,%d" % (i, node_from, links_len)