#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input) -- playhistory.csv & people.csv
    for line in sys.stdin:
        
        # remove characters 
        data = line.strip().split(',')
        printTemplate = '{0},{1},{2},{3}'

        if data[0] == 'id' or data[0] == 'track_id':
            continue

        userId = 0
        firstName = None
        lastName = None
        trackId = None

        if len(data) == 7:
            userId = int(data[0])
            firstName = data[1]
            lastName = data[2]
        elif len(data) == 3:
            trackId = data[0]
            userId = int(data[1])
        else:
            continue

        print(printTemplate.format(userId, firstName, lastName, trackId))

mapper()