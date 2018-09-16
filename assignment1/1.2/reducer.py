#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    previousUserId = None
    currentUserId = None
    currentHourOfDay = None
    firstName = None
    lastName = None
    printTemplate = '{0};{1};{2};{3}'
    tracksPerHour = {}

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')

        if len(data) > 4:
            continue

        currentUserId = data[0]
        currentFirstName = data[1] if data[1] != 'None' else None
        currentLastName = data[2] if data[2] != 'None' else None
        currentHourOfDay = data[3] if data[3] != 'None' else None
        listenCount = 1

        if previousUserId and previousUserId != currentUserId:
            for hour in sorted(tracksPerHour.keys()):
                print(printTemplate.format(firstName, lastName, hour, tracksPerHour[hour]))

            firstName = None
            lastName = None
            tracksPerHour.clear()

        if currentHourOfDay:
            if tracksPerHour.has_key(currentHourOfDay):
                tracksPerHour[currentHourOfDay] += listenCount
            else:
                tracksPerHour[currentHourOfDay] = listenCount

        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

        previousUserId = currentUserId
   
    # Print the last user and the count
    for hour in sorted(tracksPerHour.keys()):
        print(printTemplate.format(firstName, lastName, hour, tracksPerHour[hour]))

reducer()