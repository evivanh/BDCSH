#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    previousUserId = None
    currentUserId = None
    previousHourOfDay = None
    currentHourOfDay = None
    previousAmountPerHour= 0
    currentAmountPerHour = 0
    previousFirstName = None
    previousLastName = None
    currentFirstName = None
    currentLastName = None
    printTemplate = '{0};{1};{2};{3};{4}'

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')

        if len(data) < 4:
            continue

        currentUserId = data[0]
        currentFirstName = data[1] if data[1] != None else None
        currentLastName = data[2] if data[2] != None else None
        currentHourOfDay = data[3] if data[3] != None else None
        currentAmountPerHour = 1

        # if currentFirstName and previousFirstName == None:
        #     previousFirstName = currentFirstName

        # if currentLastName and previousLastName == None:
        #     previousLastName = currentLastName

        # if previousUserId and previousUserId != currentUserId:
        #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #     previousAmountPerHour = 0
        #     previousUserId = None
        #     previousFirstName = None
        #     previousLastName = None
        #     previousHourOfDay = None
        # if currentHourOfDay and currentHourOfDay == previousHourOfDay:
        #     previousAmountPerHour += currentAmountPerHour
        # if currentHourOfDay and previousHourOfDay and previousHourOfDay != currentHourOfDay:
        #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #     previousHourOfDay = currentHourOfDay
        #     previousAmountPerHour = 0

        # if previousUserId != currentUserId and currentFirstName and currentLastName:
        #     previousFirstName = currentFirstName
        #     previousLastName = currentLastName


        # previousUserId = currentUserId


        last valid stuff
        if previousUserId and previousUserId != currentUserId:
            print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousAmountPerHour = 0
            previousUserId = None
            previousFirstName = None
            previousLastName = None
            previousHourOfDay = None
        # maybe good
        if previousUserId == currentUserId and currentHourOfDay and previousHourOfDay and previousHourOfDay != currentHourOfDay:
            print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousHourOfDay = currentHourOfDay
            previousAmountPerHour = 0
        # good
        if previousUserId != currentUserId and currentFirstName and currentLastName:
            previousFirstName = currentFirstName
            previousLastName = currentLastName
        if previousUserId == currentUserId and currentHourOfDay:
            previousHourOfDay = currentHourOfDay
            previousAmountPerHour += currentAmountPerHour
        # if previousUserId == currentUserId and currentFirstName and currentLastName:
        #     previousFirstName = currentFirstName
        #     previousLastName = currentLastName
        previousUserId = currentUserId
        # previousFirstName = currentFirstName
        # previousLastName = currentLastName
        # previousHourOfDay = currentHourOfDay
   
    # Print the current word and its count
    if previousFirstName and previousLastName and previousHourOfDay and previousAmountPerHour:
        print("third")
        print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))

reducer()