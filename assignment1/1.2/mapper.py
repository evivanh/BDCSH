#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:
        
        # remove characters 
        data = line.split(',')
        
        # wrong
        if len(data) != 3 or len(data) != 7:
            continue

        if len(data) == 3:
            if data[0] == 'track_id' or data[1] == 'user' or data[2] == 'datetime':
                continue 

        if len(data) == 7:
            if data[0] == 'id' or data[1] == 'first_name' or data[2] == 'last_name':
                continue



        

        # print the trackId, date and amount
        # print('{0};{1};{2}'.format(trackId, monthYear, amount))

mapper()