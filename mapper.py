#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    word = "fantastic"

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        row = ''.join(e for e in line if e.isalnum())

        row.lower()

        if word in row:
            print("{0}".format(word))

mapper()