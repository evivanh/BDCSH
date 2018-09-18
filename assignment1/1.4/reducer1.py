#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    userId = None
    firstName = None
    lastName = None
    printTemplate = '{0},{1},{2},{3},{4}'
    userTracks = {}

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(',')

        if len(data) > 4:
            continue

        # output : userid , first, last, 1 track, hoevaak 1 track
        # hoevaak track geluisterd pp
        currentUserId = data[0]
        currentFirstName = data[1] if data[1] != 'None' else None
        currentLastName = data[2] if data[2] != 'None' else None
        currentTrackId = data[3] if data[3] != 'None' else None
        listenCount = 1


        if userId and userId != currentUserId:
            for track, amount in userTracks.items():
                print(printTemplate.format(userId, firstName, lastName, track, amount))

            firstName = None
            lastName = None
            currentTrackId = None
            userTracks.clear()

        if currentTrackId:
            if currentTrackId in userTracks:
                userTracks[currentTrackId] += listenCount
            else:
                userTracks[currentTrackId] = listenCount

        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

        userId = currentUserId
   
    # Print the last user and the count
    for track, amount in sorted(userTracks.items()):
        print(printTemplate.format(userId, firstName, lastName, track, amount))

reducer()


