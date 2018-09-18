#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input) -- import output from first reducer and tracks.csv
    for line in sys.stdin:
        
        # remove characters 
        data = line.strip().split(',')
        printTemplate = '{0},{1},{2},{3},{4},{5}'

        if data[0] == 'track_id':
            continue


        userId = 0
        firstName = None
        lastName = None
        trackId = None
        trackCount = 0
        artist = None

        if len(data) == 5:
            userId = int(data[0])
            firstName = data[1]
            lastName = data[2]
            trackId = data[3]
            trackCount = int(data[4])
        elif len(data) == 4:
            trackId = data[0]
            artist = data[1]
        else:
            continue

        print(printTemplate.format(trackId, userId, firstName, lastName, trackCount, artist))

mapper()