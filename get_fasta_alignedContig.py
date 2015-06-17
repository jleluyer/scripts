#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2012-08-23

"""
usage:
keep_contig.py Aligned_contigs.txt 454AllContigs.fna
"""

class Printer:
	def __init__ (self, contigName):
		self.printing = False
		self.contigList = []
		for id in open(contigName):
			self.contigList.append(id.strip())

	def parseLine(self, line):
		if '>' in line:
			tokens = line.strip().split()
			if tokens[0][1:] in self.contigList:
				self.printing = True
				print line.strip()
			else:
				self.printing = False
		else:
			if self.printing == True:
				print line.strip()


import sys

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print __doc__
		sys.exit(1)

	contigName=sys.argv[1]
	printer = Printer(contigName)
	filename=sys.argv[2]
	for line in open(filename):		
		printer.parseLine(line)
