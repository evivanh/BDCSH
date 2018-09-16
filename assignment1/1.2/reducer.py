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

        if len(data) < 4:
            continue

        currentUserId = data[0]
        currentFirstName = data[1] if data[1] != None else None
        currentLastName = data[2] if data[2] != None else None
        currentHourOfDay = data[3] if data[3] != None else None
        listenCount = 1

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


        # Changed user?
        if previousUserId and previousUserId != currentUserId:
            # Print previous last line
            print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            # Reset vars
            previousAmountPerHour = 0
            previousUserId = None
            previousFirstName = None
            previousLastName = None
            previousHourOfDay = None

        # Same user but hour of day changed?
        # if previousUserId == currentUserId and previousHourOfDay and previousHourOfDay != currentHourOfDay:
        #     # Print current user and previous hour of day
        #     print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
        #     # Reset var
        #     previousAmountPerHour = 0
        
        # Set name of current user
        if currentFirstName and currentLastName:
            previousFirstName = currentFirstName
            previousLastName = currentLastName
        
        # If line has an hour of day
        if currentHourOfDay:
            previousHourOfDay = currentHourOfDay
            # Same user and hour of day? Increase count
            if previousUserId == currentUserId and previousHourOfDay == currentHourOfDay:
                previousAmountPerHour += listenCount
            elif previousHourOfDay != currentHourOfDay:
                # Print current user and previous hour of day
                print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
                # Reset var
                previousAmountPerHour = 0

        previousUserId = currentUserId
   
    # Print the current word and its count
    if previousFirstName and previousLastName and previousHourOfDay and previousAmountPerHour:
        print(printTemplate.format(previousUserId, previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))

reducer()