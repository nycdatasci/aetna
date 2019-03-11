#!/usr/bin/env python

import sys
pop_table_path = 'pop_table'
nodeVal = {}
for line in open(pop_table_path):
	key, value = line.strip().split('\t')
	nodeVal[key] = float(value)
num = len(nodeVal)


for line in sys.stdin:
	nodes = line.strip().split('\t')
 	node_from = nodes[0]
 	node_to = nodes[1:]
 	links_len = len(node_to)
 	if links_len > 0:
 	    for i in node_to:
 		print("%s\t%f" % (i, 1.0 / links_len * nodeVal[node_from]))
