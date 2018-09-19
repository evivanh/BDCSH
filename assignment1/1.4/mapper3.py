#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input) -- import output from reducer2 = track id, user id, first name, last name, count and artist
    for line in sys.stdin:
        
        # remove characters 
        data = line.strip().split(',')
        printTemplate = '{0},{1},{2},{3},{4}'

        userId = 0
        firstName = None
        lastName = None
        trackCount = 0
        artist = None

        if len(data) == 6:
            userId = int(data[1])
            firstName = data[2]
            lastName = data[3]
            trackCount = int(data[4])
            artist = data[5]
        else:
            continue

        print(printTemplate.format(userId, firstName, lastName, trackCount, artist))

mapper()