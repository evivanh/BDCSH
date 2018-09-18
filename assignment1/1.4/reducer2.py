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

        currentUserId = data[0]
        currentTrackId = data[1] if data[1] != 'None' else None
        currentFirstName = data[2] if data[2] != 'None' else None
        currentLastName = data[3] if data[3] != 'None' else None
        currentTrackCount = data[4]
        currentArtist = data[5] if data[5] != 'None' else None

        # print("currents ", currentTrackId, currentUserId, currentFirstName, currentLastName, currentTrackCount, currentArtist)
        # print ("previ ", userId, firstName, lastName)

        if userId and userId != currentUserId:
            # print("u ", userId , " ",  currentUserId)
            # print("len " , len(userTracks))
            # print(userTracks.items())
            # print(userTracks)
            for track in userTracks.items():
                print(printTemplate.format(userId, firstName, lastName, track[0], track[1][INDEX_TRACK_COUNT], track[1][INDEX_TRACK_ARTIST]))

            firstName = None
            lastName = None
            currentTrackId = None
            userTracks.clear()

        if currentTrackId:
            if currentTrackId in userTracks:
                if currentTrackCount:
                    userTracks[currentTrackId][INDEX_TRACK_COUNT] = currentTrackCount

                if currentArtist:
                    print("currentartist ")
                    userTracks[currentTrackId][INDEX_TRACK_ARTIST] = currentArtist
            else: 
                userTracks[currentTrackId] = [0, None]



        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

        userId = currentUserId
   
    # Print track id, user id, first name, last name, count and artist combined per track
    for track in userTracks.items():
        print(printTemplate.format(userId, firstName, lastName, track[0], track[1][INDEX_TRACK_COUNT], track[1][INDEX_TRACK_ARTIST]))

reducer()


