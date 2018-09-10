#!/usr/bin/python
"""mapper.py"""

import sys
import re

def mapper():

    # Input comes from STDIN (standard input)
    for line in sys.stdin:

        # remove characters 
        row = line.split()
        print (row)
        # row = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', line)
        # row.split('"', row)
        # print(line)

        for word in row:

            for ch in "['#','`','\','-','=','!','\N','\n','\t','?', '"']":
                if ch in word:
                    word = word.replace(ch, '')
                    print(word)

            print('{0}\t{1}'.format(word.lower(), 1))

mapper()