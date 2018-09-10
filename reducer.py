#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    template = "{0};{1};"

    previousWord = None
    currentWord = None
    amountPreviousWord = 0
    amountWord = 0

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')
        if len(data) != 2:
            continue

        currentWord = data[0]
        amountWord = int(data[1])

        # check if previousWord exists and not the same as current
        if previousWord and previousWord != currentWord:
            #print previous word and reset
            print(template.format(previousWord, amountPreviousWord))
            previousWord = None
            amountPreviousWord = 0

        # if previous word and current word are the same, add to counter and previous word is current word
        amountPreviousWord += amountWord
        previousWord = currentWord
   
    # Print the current word and its count
    print(template.format(previousWord, amountWord))
   
        

reducer()