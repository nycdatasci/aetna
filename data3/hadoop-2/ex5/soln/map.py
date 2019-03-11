#!/usr/bin/env python

import sys
country_path = 'country'
countries = {}
for line in open(country_path):
	value, key = line.strip().split('|')
	countries[key] = value


for line in sys.stdin:
	name, comment, country = line.strip().split('|')
	country_name = countries[country]
	key = country_name + ',' + comment
 	print "%s\t%d" % (key, 1)