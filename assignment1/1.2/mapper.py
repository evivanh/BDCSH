#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:
        
        # remove characters 
        data = line.split(',')

        # if longer than 7 delete
        if len(data) > 7:
            continue

        if data[0] == 'id' or data[1] == 'first_name' or data[2] == 'last_name' or data[0] == 'track_id' or data[1] == 'user' or data[2] == 'datetime':
            continue

        user_id = 0
        first_name = None
        last_name = None
        hourOfDay = None

        if len(data) == 7:
            user_id = int(data[0])
            first_name = data[1]
            last_name = data[2]

        if len(data) == 3:
            user_id = int(data[1])
            hourOfDay = data[2][11:13]

        print('{0};{1};{2};{3}'.format(user_id, first_name, last_name, hourOfDay))


mapper()