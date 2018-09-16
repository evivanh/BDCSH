#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    previousUserId = None
    currentUserId = None
    previousHourOfDay = None
    currentHourOfDay = None
    previousAmountPerHour = 0
    previousFirstName = None
    previousLastName = None
    currentFirstName = None
    currentLastName = None
    printTemplate = '{0};{1};{2};{3};{4}'

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')

        if len(data) > 4:
            continue

        currentUserId = data[0]
        currentFirstName = data[1]
        currentLastName = data[2]
        currentHourOfDay = data[3]
        listenCount = 1

        # if currentFirstName and previousFirstName == None:
        #     previousFirstName = currentFirstName

        # if currentLastName and previousLastName == None:
        #     previousLastName = currentLastName

        if previousUserId != currentUserId:
            print("first")
            if previousUserId != None:
                print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousAmountPerHour = 0
            previousUserId = currentUserId
            if currentFirstName and currentLastName:
                print("second ", currentFirstName, currentLastName)
                previousFirstName = currentFirstName
                previousLastName = currentFirstName
            if currentHourOfDay:
                print("third ", currentHourOfDay)
                previousHourOfDay = currentHourOfDay
        if currentHourOfDay and currentHourOfDay == previousHourOfDay:
            print("fifth")
            previousAmountPerHour += listenCount
        if currentHourOfDay and previousHourOfDay != currentHourOfDay:
            print("sixth")
            print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousHourOfDay = currentHourOfDay
            previousAmountPerHour = 0
        if previousUserId == currentUserId and currentFirstName and currentLastName:
            print("seventh")
            previousFirstName = currentFirstName
            previousLastName = currentLastName


        previousUserId = currentUserId


        # # Changed user?
        # if previousUserId and previousUserId != currentUserId:
        #     # Print previous last line
        #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #     # Reset vars
        #     previousAmountPerHour = 0
        #     previousUserId = None
        #     previousFirstName = None
        #     previousLastName = None
        #     previousHourOfDay = None

        # # Same user but hour of day changed?
        # # if previousUserId == currentUserId and previousHourOfDay and previousHourOfDay != currentHourOfDay:
        # #     # Print current user and previous hour of day
        # #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        # #     # Reset var
        # #     previousAmountPerHour = 0
        
        # # Set name of current user
        # if currentFirstName and currentLastName:
        #     previousFirstName = currentFirstName
        #     previousLastName = currentLastName
        
        # # If line has an hour of day
        # if currentHourOfDay:
        #     # Same user and hour of day? Increase count
        #     if previousUserId == currentUserId and previousHourOfDay == currentHourOfDay:
        #         previousAmountPerHour += listenCount
        #     elif previousHourOfDay != currentHourOfDay:
        #         # Print current user and previous hour of day
        #         print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #         # Reset var
        #         previousAmountPerHour = 0

        #     previousHourOfDay = currentHourOfDay

        # previousUserId = currentUserId
   
    # Print the current word and its count
    if previousFirstName and previousLastName and previousHourOfDay and previousAmountPerHour:
        print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))

reducer()