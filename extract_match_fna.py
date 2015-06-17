#!/usr/bin/python
# encoding: utf-8
#author: Charles Joly Beauparlant
# 2012-08-23

"""
usage:
keep_hsapiens.py singletonFilename filename.fa
"""

class Printer:
	def __init__ (self, singletonName):
		self.printing = False
		self.singletonList = []
		for id in open(singletonName):
			self.singletonList.append(id.strip())
	def lineContainID(self, line):
		for id in self.singletonList:
			if id in line:
				return True
		return False

	def parseLine(self, line):
			if self.lineContainID(line) == True:
				self.printing = True
				print line.strip()
			else:
				self.printing = False


import sys

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print __doc__
		sys.exit(1)

	singletonName=sys.argv[1]
	printer = Printer(singletonName)
	filename=sys.argv[2]
	for line in open(filename):		
		printer.parseLine(line)
