#!/usr/bin/python

"""
usage:
fileTrim.py fileToTrim
"""

import sys

filename = sys.argv[1]
contigList = []
for line in open(filename):
        contig = line.split()[0]
        if contig not in contigList:
                contigList.append(contig)
                print line.strip()
