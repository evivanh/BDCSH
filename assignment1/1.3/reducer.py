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
    #tracksInHour ={}
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


        if  title  and artist:
            currentTitle = title
            currentArtist = artist
        if trackId in trackInfo:
            #add artist and title to trackid and counter
            trackInfo[trackId][0]=currentArtist
            trackInfo[trackId][1] =currentTitle

        else:
            #make a new key(trackid) and add currentArtist and currentTitle
            trackInfo[trackId] = [currentArtist, currentTitle,0]    
        

        if hour == 1:
            if trackId in trackInfo:
            #add counter to trackId, currentArtist and currentTitle
                trackInfo[trackId][2]+= 1
            else:
            #make a new key(trackId) and add trackid and counter
                trackInfo[trackId]=[None, None, 1]


    for track in sorted(trackInfo.items(), key=lambda x:x[1][2], reverse= True)[0:5]:
        print('{0}\t{1}\t{2}'.format(track[1][0], track[1][1], track[1][2]))


reducer()