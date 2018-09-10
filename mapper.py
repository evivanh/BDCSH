#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        data = line.split('\t')

        if len(data) != 5:
            continue

        body = data[4]
        
        for ch in ['.',',','!','?',':',';','"','(',')','<','>','[',']','#','$','=','-','/']:
            if ch in body:  
                body = body.replace(ch," ")

        body = body.split()
        
        for word in body:
            # if not a numeric character remove
            # word = ''.join(e for e in word if e.isalnum())

           

            # if word not empty print
            if word:
                print('{0};{1}'.format(word.lower(), 1))

mapper()