#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:
        
        # remove characters 
        data = line.split(',')
        # print (data)
        # wrong
        if len(data) > 7:
            continue

        if data[0] == 'track_id' or data[1] == 'user' or data[2] == 'datetime' or data[0] == 'id' or data[1] == 'first_name' or data[2] == 'last_name':
            print(data[0])
            continue

        # print(data[0])

        

        # print the trackId, date and amount
        print('{0};{1};{2}'.format(data[0], data[1], data[2]))

mapper()