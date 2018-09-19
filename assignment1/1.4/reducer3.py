#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    userId = None
    firstName = None
    lastName = None
    printTemplate = '{0},{1},{2},{3},{4}'
    userListenedToArtist = {}

    # Input comes from STDIN
    # format is user id, first name, last name, track count, artist
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(',')

        if len(data) != 5:
            continue

        # dict VAN TRACKS van user > key is artiest >  count
        # veranderd van user : sort je op count desc en pak je bovenste en print

        currentUserId = int(data[0])
        currentFirstName = data[1] if data[1] != 'None' else None
        currentLastName = data[2] if data[2] != 'None' else None
        currentTrackCount = int(data[3])
        currentArtist = data[4] if data[4] != 'None' else None

        if userId and currentUserId != userId:
            artist = sorted(userListenedToArtist.items(), key=lambda x:x[1], reverse = True)[:1]
            print(printTemplate.format(firstName, lastName, artist[0], artist[1]))

            firstName = None
            lastName = None
            userListenedToArtist.clear()

        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

        if currentArtist:
            if currentArtist in userListenedToArtist:
                userListenedToArtist[currentArtist] += currentTrackCount
            else:
                userListenedToArtist[currentArtist] = currentTrackCount

        userId = currentUserId
   
    # Print track id, user id, first name, last name, count and artist combined per track
    artist = sorted(userListenedToArtist.items(), key=lambda x:x[1], reverse = True)[:1]
    print(printTemplate.format(firstName, lastName, artist[0], artist[1]))

reducer()


