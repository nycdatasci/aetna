#!/usr/bin/env python

import sys

def mapper():
    for record in sys.stdin:
        try:
            _, _, user_id, rating, _, _ = record.split(',', 5)
            if user_id.isdigit():
                print '{0}\t{1}'.format(user_id, rating.strip())
        except:
            pass

if __name__ == '__main__':
    mapper()
