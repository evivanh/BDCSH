#!/usr/bin/python
"""reducer.py"""

import sys

def reducer():

    template = "{0};{1};{2};{3};{4}"

    prevMunicipality = None
    currentMunicipality = None
    currentMunicipalityMale = 0
    currentMunicipalityFemale = 0
    currentMunicipalityTotal = 0
    currentMunicipalityCostsCare = 0

    # Input comes from STDIN
    for line in sys.stdin:

        # Check argument count
        data = line.strip().split(';')
        if len(data) != 4:
            continue

        currentMunicipality = data[0]
        males = int(data[1])
        females = int(data[2])
        costCare = float(data[3])

        # If current municipality does not equal previous municipality
        if prevMunicipality and prevMunicipality != currentMunicipality:

            # Print the previous municipality and its count
            print(template.format(prevMunicipality, currentMunicipalityTotal, currentMunicipalityMale, currentMunicipalityFemale, currentMunicipalityCostsCare))

            # Reset counters
            currentMunicipalityMale = 0
            currentMunicipalityFemale = 0
            currentMunicipalityTotal = 0
            currentMunicipalityCostsCare = 0

            # New current word
            prevMunicipality = currentMunicipality

        # Increase counters
        currentMunicipalityMale += males
        currentMunicipalityFemale += females
        currentMunicipalityTotal = currentMunicipalityMale + currentMunicipalityFemale
        currentMunicipalityCostsCare += costCare
        
        # Set the current word as the previous word for next iteration
        prevMunicipality = currentMunicipality

    # Print the current word and its count
    print(template.format(prevMunicipality, currentMunicipalityTotal, currentMunicipalityMale, currentMunicipalityFemale, currentMunicipalityCostsCare))

reducer()