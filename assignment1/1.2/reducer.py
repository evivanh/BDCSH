#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    previousUserId = None
    currentUserId = None
    previousHourOfDay = None
    currentHourOfDay = None
    previousAmountPerHour = 0
    firstName = None
    lastName = None
    printTemplate = '{0};{1};{2};{3};{4}'
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
                print(printTemplate.format(previousUserId, firstName, lastName, hour, tracksPerHour[hour]))

            firstName = None
            lastName = None
            previousAmountPerHour = 0
            previousUserId = currentUserId
            previousHourOfDay = None
            tracksPerHour.clear()
            # if currentHourOfDay:

            #     previousHourOfDay = currentHourOfDay
            # else: 
            #     previousHourOfDay = None

        if currentHourOfDay:
            if tracksPerHour.has_key(currentHourOfDay):
                tracksPerHour[currentHourOfDay] += listenCount
            else:
                tracksPerHour[currentHourOfDay] = listenCount

            
            
            
       
        # if currentHourOfDay and currentHourOfDay == previousHourOfDay:
        #     # print("fifth")
        #     previousAmountPerHour += listenCount
        # if currentHourOfDay and previousHourOfDay != currentHourOfDay:
        #     # print("sixth")
        #     if previousHourOfDay != None:
        #         print(printTemplate.format(previousUserId, firstName, lastName, previousHourOfDay, previousAmountPerHour))
        #     previousHourOfDay = currentHourOfDay
        #     previousAmountPerHour = 0


        if currentFirstName and currentLastName:
            firstName = currentFirstName
            lastName = currentLastName

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
    if firstName and lastName and previousHourOfDay and previousAmountPerHour:
        for hour in sorted(tracksPerHour.keys()):
            print(printTemplate.format(previousUserId, firstName, lastName, hour, tracksPerHour[hour]))

reducer()