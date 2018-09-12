#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:
        
        # remove characters 
        data = line.split(',')
        
        # wrong
        if len(data) < 3:
            continue

        trackId = data[0]
        monthYear = data[2][0:7]
        amount = 1

        if trackId == 'track_id' or data[1] == 'user' or data[2] == 'datetime':
            continue

        # print the trackId, date and amount
        print('{0};{1};{2}'.format(trackId, monthYear, amount))

mapper()