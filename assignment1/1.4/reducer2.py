#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    trackId = None
    artist = None
    printTemplate = '{0},{1},{2},{3},{4},{5}'
    usersListenedToTrack = []

    # Input comes from STDIN
    # format is track id, user id, first name, last name, track count, artist
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(',')

        if len(data) != 6:
            continue

        currentUserId = int(data[1])
        currentTrackId = data[0] if data[0] != 'None' else None
        currentFirstName = data[2] if data[2] != 'None' else None
        currentLastName = data[3] if data[3] != 'None' else None
        currentTrackCount = int(data[4])
        currentArtist = data[5] if data[5] != 'None' else None

        # print("currents ", currentTrackId, currentUserId, currentFirstName, currentLastName, currentTrackCount, currentArtist)
        # print ("previ ", userId, firstName, lastName)
        if trackId and currentTrackId != trackId:
            for user in usersListenedToTrack:
                print(printTemplate.format(trackId, user[0], user[1], user[2], user[3], artist))

            artist = None
            usersListenedToTrack = []

        if currentUserId:
            usersListenedToTrack.append([currentUserId, currentFirstName, currentLastName, currentTrackCount])
        
        if currentArtist:
            artist = currentArtist

        trackId = currentTrackId
   
    # Print track id, user id, first name, last name, count and artist combined per track
    for user in usersListenedToTrack:
        print(printTemplate.format(trackId, user[0], user[1], user[2], user[3], artist))

reducer()


