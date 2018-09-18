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
            for track in userTracks.items():
                print(printTemplate.format(track, userId, firstName, lastName, userTracks[track][INDEX_TRACK_COUNT], userTracks[track][INDEX_TRACK_ARTIST]))

            firstName = None
            lastName = None
            currentTrackId = None
            userTracks.clear()

        if currentTrackId:
            if currentTrackId not in userTracks:
                print("hello")
                userTracks[currentTrackId] = [0, None]
            if currentTrackCount:
                print("track id ", userTracks[currentTrackId])
                userTracks[currentTrackId][INDEX_TRACK_COUNT] = currentTrackCount
            if currentArtist:
                userTracks[currentTrackId][INDEX_TRACK_ARTIST] = currentArtist

        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

        userId = currentUserId
   
    # Print track id, user id, first name, last name, count and artist combined per track
    for track in sorted(userTracks.items()):
        print(printTemplate.format(track, userId, firstName, lastName, userTracks[track][INDEX_TRACK_COUNT], userTracks[track][INDEX_TRACK_ARTIST]))

reducer()


