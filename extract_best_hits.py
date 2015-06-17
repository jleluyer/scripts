#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-08-19

import sys

species_list = []

oldLine=""
state = "lookingForEntry"
count = 0
for line in sys.stdin:
        count += 1
        if count % 100000 == 0:
                sys.stderr.write("Line processed: " + str(count) + "\n")
        if state == "lookingForEntry" and len(line.split()) > 2:
                if line.split()[0] == "Sequences" and line.split()[1]== "producing":
                        state = "entryFound"
        elif state == "entryFound" and len(line) > 0:
                if line[0] == '>':
                        if '[' in line:
                                specie_1 = line.split('[')[1].strip()
                                if ']' in specie_1:
					species_list.append(specie_1.split(']')[0])
                                        state = "lookingForEntry"
                                if ']' not in specie_1:
                                        state = "parsedFirstPart"
                        if '[' not in line:
                                state = "allOnSecondLine"
                                oldLine = line.strip()
        elif state == "parsedFirstPart":
                specie_2 = line.split(']')[0]
                species_list.append(specie_1 + " " + specie_2)
                state = "lookingForEntry"
        elif state == "allOnSecondLine" and len(line) > 0:
                if '[' in line:
                        specie = line.split('[')[1].split(']')[0]
                        species_list.append(specie)
                if '[' not in line:
                        if "human" in line.strip().lower() or "human"in oldLine:
                                species_list.append("Human")
                		state = "lookingForEntry"

#print "count: " + str(len(species_list))
for specie in species_list:
        print specie
