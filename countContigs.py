#!/usr/bin/env python


"""
usage:
countContigs.py 454file
"""
import sys

contigsHash = {}
for line in open(sys.argv[1], 'r'):
    array=line.split('\t')

    if contigsHash.has_key(array[2]):
        contigsHash[array[2]] += 1
    else:
        contigsHash[array[2]] = 1

for key in contigsHash.keys():
    print key, contigsHash[key]
