#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    previousTrack = None
    currentTrack = None
    previousDate = None
    currentDate = None
    previousAmountTrack= 0
    currentAmountTrack = 0

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')
        if len(data) < 3:
            continue

        currentTrack = data[0]
        currentDate = data[1]
        currentAmountTrack = data[2]

        # check trackid first
        if previousTrack and previousTrack != currentTrack:
            print('{0};{1};{2}'.format(previousTrack, previousDate, previousAmountTrack))
            previousAmountTrack = 0

        # check dates 
        if previousDate and previousDate != currentDate:
            print('{0};{1};{2}'.format(previousTrack, previousDate, previousAmountTrack))
            previousAmountTrack = 0

         # if previous track and data are the same as current, add to counter and previous track is current track
        previousAmountTrack += currentAmountTrack
        previousTrack = currentTrack
        previousDate = currentDate
   
    # Print the current word and its count
    print('{0};{1};{2}'.format(previousTrack, previousDate, previousAmountTrack))
   
        

reducer()