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
        currentFirstName = data[1]
        currentLastName = data[2]
        currentHourOfDay = int(data[3])
        currentAmountPerHour = 1

        # check trackid 
        if previousUserId and previousUserId != currentUserId:
            print(printTemplate.format(previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousAmountPerHour = 0

        # check dates 
        if previousUserId == currentUserId and previousHourOfDay and previousHourOfDay != currentHourOfDay:
            print(printTemplate.format(previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))
            previousAmountPerHour = 0
        
        if previousUserId == currentUserId and currentHourOfDay and previousHourOfDay == currentHourOfDay:
            previousAmountPerHour =+ currentAmountPerHour
            previousHourOfDay = currentHourOfDay

        if previousUserId == currentUserId:
            previousFirstName = currentFirstName
            previousLastName = currentLastName
    
        previousUserId = currentHourOfDay
   
    # Print the current word and its count
    print(printTemplate.format(previousFirstName, previousLastName, previousHourOfDay, previousAmountPerHour))

reducer()