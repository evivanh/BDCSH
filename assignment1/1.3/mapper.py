#!/usr/bin/python
"""mapper.py"""

import sys


def mapper():

    HOUR_OF_DAY = 19
    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters
        data = line.strip().split(',')

        if data[0] == 'track_id' or data[1] == 'artist' or data[2] == 'title' or data[0] == 'track_id' or data[2] == 'datetime':
            continue

        trackId = None
        artist = None
        title = None
        dateTime = None
        trackPlayedCounter = 0

        if len(data) == 4:
            trackId = data[0]
            artist = data[1]
            title = data[2]
            print('{0};{1};{2};{3}'.format(trackId, artist, title, trackPlayedCounter))    
        elif len(data) == 3:
            trackId = data[0]
            dateTime = int(data[2][11:13])
        if dateTime == HOUR_OF_DAY:
            trackPlayedCounter = 1
            print('{0};{1};{2};{3}'.format(trackId, artist, title, trackPlayedCounter))   	 
        else:
            continue
mapper()
