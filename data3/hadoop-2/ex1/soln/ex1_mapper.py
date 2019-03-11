#!/usr/bin/env python

import sys
from datetime import datetime as dt

n = 10

def compare(x, y):
    _, _, _, _, datex, _ = x.split(',', 5)
    _, _, _, _, datey, _ = y.split(',', 5)
    datex = dt.strptime(datex, '%Y/%m/%d')
    datey = dt.strptime(datey, '%Y/%m/%d')
    return datex > datey

def order_list(L, i = -1):
    for i in range(i, -len(L), -1):
        if compare(L[i], L[i-1]):
            L[i], L[i-1] = L[i-1], L[i]
        else:
            return

def mapper():
    top_n = [None for x in range(n)]
    free = n	
    for record in sys.stdin:
        try:
            _, _, _, rating, date, _ = record.split(',', 5)
            if rating == '5.0':
                if free:
                    top_n[-free] = record
                    order_list(top_n, -free)
                    free -= 1
                else:
                    if compare(record, top_n[-1]):
                        top_n[-1] = record
                        order_list(top_n)
        except:
            pass
    for x in top_n:
        print x

if __name__ == '__main__':
    mapper()
