#!/usr/bin/python
"""mapper.py"""

import sys
import re

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        row = line.strip()
        row = re.split(r'[`\-=!#$()+\[\];\'\\:"<,./<>?\t\N\r\n]', line)

        for word in row: 
            print(word, 1)

mapper()