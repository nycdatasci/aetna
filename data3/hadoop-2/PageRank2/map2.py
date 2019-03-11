#!/usr/bin/env python

import sys

pop_table_path = 'pop_table'
nodeVal = {}
for line in open(pop_table_path):
        key, value = line.strip().split('\t')
        nodeVal[key] = float(value)

split_val = lambda x: 1.0/int(x.split(',')[1]) * nodeVal.get(x.split(',')[0], 0)

for line in sys.stdin:
	nodes = line.strip().split('\t')
	node_to = nodes[0]
	node_from = nodes[1:]
	links_len = len(node_from)
	if links_len == 0: continue
	print "%s\t%s" % (node_to, sum(map(split_val, node_from)))
