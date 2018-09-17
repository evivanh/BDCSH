#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input) -- playhistory.csv & people.csv
    for line in sys.stdin:
        
        # remove characters 
        data = line.strip().split(',')
        printTemplate = '{0}-{1}-{2}-{3}'

        if data[0] == 'id' or data[0] == 'track_id':
            continue

        user_id = 0
        first_name = None
        last_name = None
        trackId = None

        if len(data) == 7:
            user_id = int(data[0])
            first_name = data[1]
            last_name = data[2]
        elif len(data) == 3:
            user_id = int(data[0])
            trackId = data[1]
        else:
            continue

        print(printTemplate.format(user_id, first_name, last_name, trackId))

mapper()