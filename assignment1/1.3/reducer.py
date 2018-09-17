#!/usr/bin/python
"""reducer.py"""

import sys


def reducer():

    previousTrackId = None
    previousTitle = None
    previousArtist = None
    previousHour = None

    currentTrackId = None
    currentTitle = None
    currentArtist = None
    currentHour = None
    tracksInHour = {}
    trackInfo = {}

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')

        if len(data) > 4:
            continue

        trackId = data[0] if data[0] != 'None' else None
        title = data[1] if data[1] != 'None' else None
        artist = data[2] if data[2] != 'None' else None
        hour = int(data[3])

        if title and artist:
            currentTitle = title
            currentArtist = artist

            if trackId not in trackInfo:
                trackInfo[trackId] = [currentArtist, currentTitle]

        if hour == 1:
            if trackId in tracksInHour:
                tracksInHour[trackId] += 1
            else:
               tracksInHour[trackId] = 1

        for track in sorted(tracksInHour.items(), key=lambda x: x[1], reverse=True)[0:5]:
            for info in trackInfo:
                if track[0] == info:
                    print('{0}\t{1}\t{2}'.format(trackInfo[info][0], trackInfo[info][1], track[1]))


reducer()
