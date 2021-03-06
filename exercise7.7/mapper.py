#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        data = line.split('\t')
        # wrong
        if len(data) < 5:
            continue

        body = data[4]
        
        for ch in ['.',',','!','?',':',';','"','(',')','<','>','[',']','#','$','=','-','/']:
            if ch in body:  
                body = body.replace(ch," ")

        body = body.split()
        
        for word in body:
            # if word not empty print
            if word:
                print('{0};{1}'.format(word.lower(), 1))

mapper()