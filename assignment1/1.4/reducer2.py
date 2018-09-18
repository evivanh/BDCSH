#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    userId = None
    firstName = None
    lastName = None
    printTemplate = '{0},{1},{2},{3},{4},{5}'
    userTracks = {}
    INDEX_TRACK_COUNT = 0
    INDEX_TRACK_ARTIST = 1

    # Input comes from STDIN
    # format is track id, user id, first name, last name, track count, artist
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(',')

        if len(data) > 6:
            continue

        currentTrackId = data[0] if data[0] != 'None' else None
        currentUserId = data[1]
        currentFirstName = data[2] if data[2] != 'None' else None
        currentLastName = data[3] if data[3] != 'None' else None
        currentTrackCount = data[4]
        currentArtist = data[5] if data[5] != 'None' else None

        if userId and userId != currentUserId:
            # for track in userTracks.items():
            #     print(printTemplate.format(track[0], userId, firstName, lastName, track[1][INDEX_TRACK_COUNT], track[1][INDEX_TRACK_ARTIST]))

            firstName = None
            lastName = None
            currentTrackId = None
            userTracks.clear()

        if currentTrackId:
            if currentTrackId not in userTracks:
                userTracks[currentTrackId] = [0, None]
                print ("3 " , userTracks[currentTrackId])


            print (" if " , currentTrackCount != 0 , " " , currentTrackCount)
            if currentTrackCount != 0:
                userTracks[currentTrackId][INDEX_TRACK_COUNT] = currentTrackCount
                print("1 " , userTracks[currentTrackId])
            print("artist ", currentArtist)
            if currentArtist:
                userTracks[currentTrackId][INDEX_TRACK_ARTIST] = currentArtist
                print("2 " , userTracks[currentTrackId])
   

        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

        userId = currentUserId
   
    # Print track id, user id, first name, last name, count and artist combined per track
    # for track in userTracks.items():
        # print(printTemplate.format(track[0], userId, firstName, lastName, track[1][INDEX_TRACK_COUNT], track[1][INDEX_TRACK_ARTIST]))

reducer()


