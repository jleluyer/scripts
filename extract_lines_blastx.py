#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-08-19
#usage: cat file_blastx_nr.out|./script.py > file_name.txt

import sys

lines_list = []

oldLine=""
state = "lookingForEntry"
count = 0
line_complete = ""
for line in sys.stdin:
	count += 1
	if count % 100000 == 0:
		sys.stderr.write("Line processed: " + str(count) + "\n")
	#if count == 1000000:
		#break
	if state == "lookingForEntry" and len(line.split()) > 2:
		if line.split()[0] == "Sequences" and line.split()[1] == "producing":
			state = "entryFound"
	elif state == "entryFound" and len(line) > 0:
		if line[0] == '>':
			line_complete = line
			if '[' in line:
				if ']' in line:
					lines_list.append(line_complete)
					state = "lookingForEntry"
					line_complete = ""
				if ']' not in line:
					state = "parsedFirstPart"
			elif '[' not in line:
				state = "parsedFirstPart"
	elif state == "parsedFirstPart":
		line_complete = line_complete.strip() + line
		lines_list.append(line_complete)
		state = "lookingForEntry"
		line_complete = ""

#print "count: " + str(len(species_list))
for line in lines_list:
	print line.strip()[1:]
