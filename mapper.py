#!/usr/bin/python
"""mapper.py"""

import sys

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        row = line.strip().split(';')
        # Check for the amount of columns we need
        if len(row) < 26:
            continue

        # Identify variables
        gender = row[0]
        ageGroup = row[1]
        municipality = row[2]
        amountBSN = row[3]
        costCare = row[25]

        if gender != 'M' and gender != 'V':
            continue

        # Check if age group is elderly
        minAge = ageGroup[:2]
        if minAge.isdigit() and int(minAge) >= 65:

            amountMale = amountBSN if gender == 'M' else 0
            amountFemale = amountBSN if gender == 'V' else 0

            print("{0};{1};{2};{3}".format(municipality, amountMale, amountFemale, costCare))

mapper()