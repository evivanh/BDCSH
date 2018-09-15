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

        # print("names ", previousFirstName, " ", previousLastName, " ", data[1], " ", data[2] )
        # print("b")
        # print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay))


        # if current firstname and lastname save those
        # if currentFirstName and currentLastName and previousUserId == currentUserId:




        # if currenthourofday save that

        # if previous id exists and is not the same as current id print it and reset variables
        # firstname, lastname, none, 0 fails here
        # if previousUserId and previousUserId != currentUserId:
        #     print("first")
        #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #     previousAmountPerHour = 0
        #     previousUserId = None
        #     previousFirstName = None
        #     previousLastName = None
        #     previousHourOfDay = None
        # # if previous id is same as current id and currenhour and previoushour exist and are not the same print and set previous hour of day and reset counter
        # # none, none, 01, 939 fails here
        # if previousUserId == currentUserId and currentHourOfDay and previousHourOfDay == currentHourOfDay:
        #     previousHourOfDay = currentHourOfDay
        #     previousAmountPerHour += currentAmountPerHour
        # elif previousUserId == currentUserId and currentHourOfDay and previousHourOfDay and previousHourOfDay != currentHourOfDay:
        #     print("second")
        #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #     previousHourOfDay = currentHourOfDay
        #     previousAmountPerHour = currentAmountPerHour
        # # elif previousUserId == currentUserId and currentHourOfDay and previousHourOfDay == currentHourOfDay:
        # #     previousHourOfDay = currentHourOfDay
        # #     previousAmountPerHour += currentAmountPerHour
        # # previous id is not same as curren id and current firstname and lastname exist set the names
        # if previousUserId != currentUserId and currentFirstName and currentLastName:
        #     previousFirstName = currentFirstName
        #     previousLastName = currentLastName
        # if previousUserId == currentUserId and currentFirstName and currentLastName:
        #     previousFirstName = currentFirstName
        #     previousLastName = currentLastName
        # previous id is same as current and currenthourofday exists
        # if previousUserId == currentUserId and currentHourOfDay:
        #     previousHourOfDay = currentHourOfDay
        #     previousAmountPerHour += currentAmountPerHour


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
        if previousUserId == currentUserId and currentFirstName and currentLastName:
            previousFirstName = currentFirstName
            previousLastName = currentLastName
        previousUserId = currentUserId
        # previousFirstName = currentFirstName
        # previousLastName = currentLastName
        # previousHourOfDay = currentHourOfDay
   
    # Print the current word and its count
    if previousFirstName and previousLastName and previousHourOfDay and previousAmountPerHour:
        print("third")
        print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))

reducer()