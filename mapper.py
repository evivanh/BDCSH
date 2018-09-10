#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        row = line.split('\t')
        
        for ch in "['#','`','\','-','=','!']":
            if ch in row:  
                row = row.replace(ch," ")

        row = row.split()
        
        for word in row:
            # if not a numeric character remove
            # word = ''.join(e for e in word if e.isalnum())

           

            # if word not empty print
            if word:
                print('{0};{1}'.format(word.lower(), 1))

mapper()