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
    printTemplate = '{0};{1};{2};{3}'

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

        print("names ", currentFirstName, " ", currentLastName)
        # print(printTemplate.format(currentUserId, currentFirstName, currentLastName, currentHourOfDay))
        # print("b")
        # print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay))

        if previousUserId and previousUserId != currentUserId:
            # print(printTemplate.format(previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousAmountPerHour = 0
            previousUserId = None
            previousFirstName = None
            previousLastName = None
            previousHourOfDay = None
        # maybe good
        if previousUserId == currentUserId and currentHourOfDay and previousHourOfDay and previousHourOfDay != currentHourOfDay:
            # print(printTemplate.format(previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousHourOfDay = currentHourOfDay
            previousAmountPerHour = 0
        # good
        if previousUserId != currentUserId and currentFirstName and currentLastName:
            previousFirstName = currentFirstName
            previousLastName = currentLastName
        if previousUserId == currentUserId and currentHourOfDay:
            previousHourOfDay = currentHourOfDay
            previousAmountPerHour += currentAmountPerHour

        previousUserId = currentUserId
        # previousFirstName = currentFirstName
        # previousLastName = currentLastName
        # previousHourOfDay = currentHourOfDay
   
    # Print the current word and its count
    if previousFirstName and previousLastName and previousHourOfDay and previousAmountPerHour:
        # print(printTemplate.format(previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))

reducer()