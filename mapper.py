#!/usr/bin/python
"""mapper.py"""

import sys
import re

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        row = line.strip()
        print (row)
        row = re.split(r'[`\-=!#$()+\[\];\'\\:"<,./<>?\t\r\n\N]', row)
        # print(line)
        # for word in row: 
        #     print('{0}\t{1}'.format(word.lower(), 1))

mapper()