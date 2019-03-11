#! /usr/bin/env python

import sys
import re

def cleaner(line):
    return re.sub(r'[^a-zA-Z\s\']', ' ', line).strip().lower()

def mapper():

    for record in sys.stdin:
        try:
            verse, words = record.strip().split(' ', 1)
            nums = verse.split(':')
            if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
                for word in cleaner(words).split():
                    print('{0}\t{1}'.format(word, verse))
        except:
            pass


if __name__ == '__main__':
    mapper()
