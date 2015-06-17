#!/usr/bin/python
import sys

def getORFLength(sequence, index):
	for i in range(index+1, len(sequence)-2):
		if (i - index) % 3 == 0:
			codon = sequence[i:i+3]
			if codon == "TAA" or codon == "TAG" or codon == "TGA":
				return (i - index) / 3
	return -((i - index) / 3)

def getLongestORF(sequence):
	maxLength = 0
	maxIncomplete = 0
	# For every codon
	for i in range(0, len(sequence)-2):
		codon = sequence[i:i+3]
		if codon == "ATG":
			length = getORFLength(sequence, i)
			if length > maxLength:
				maxLength = length
			if length < 0:
				if (-1 * length) > maxLength and length < maxIncomplete:
					maxIncomplete = length

	if (-1 * maxIncomplete) > maxLength:
		return maxIncomplete
	else:
		return maxLength

filename = sys.argv[1]

name = ""
sequence = ""
count = 0
for line in open(filename):
	if ">" in line:
		name = line.strip()
		if count > 0:
			print name
			print getLongestORF(sequence)
			sequence = ""
	else:
		sequence += line.strip()
	count += 1

print name
print getLongestORF(sequence)
