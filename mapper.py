#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    word = "fantastic"

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        row = line.strip().split('.', ',', '!', '?', ':', ';', '"', '(', ')', '<', '>', '[', ']', '#', '$', '=', '-','/' )

        row.lower()

        if word in row:
            print("{0}".format(word))

mapper()