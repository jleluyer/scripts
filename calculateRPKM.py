#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-07-30

import sys

if len(sys.argv)!=3:
	print "This script will calculate the RPKM for each contig."
	print ""
	print ""
	print "Usage "
	print "calculateRPKM.py <Contigs.fasta> <AlignedReads.sam> > <out>"
	print "	Contigs.fasta: List of length_contigs produced by the assembler (in fasta format)."
	print "	AlignedReads.sam: Raw files aligned against <Contigs.fasta> (in sam format)."
	print "	out: Name of the output file. Format -> 2 columns: contig_name and RPKM."
	print ""
	sys.exit()

file_length_contigs = sys.argv[1]
file_align = sys.argv[2]

# 1. Calculate the total number of aligned reads.
count = 0
for line in open(file_align):
	if line[0] != '@':
		count += 1
# 2. Parse every length_contigs and calculate their length.
length_contigs = {}
count_contigs = {}
length_contig = 0
for line in open(file_length_contigs):
	if line [0] == '>':
		if length_contig > 0:
			length_contigs[name_contig] = length_contig
		name_contig = line.split('>')[1].split()[0]
		length_contigs[name_contig] = 0
		count_contigs[name_contig] = 0
		length_contig = 0 
	else:
		length_contig += len(line.strip())
	

# 3. Parse the alignement file and count the number of reads for each length_contigs.
for line in open(file_align):
	if line[0] != '@' and line.strip().split()[2] != "*":
		count_contigs[line.strip().split()[2]] += 1

#for contig in length_contigs:
	#print contig + ": " + str(length_contigs[contig])

# 4. Calculate the RPKM value for each contig and print it out.
# http://seqanswers.com/forums/showthread.php?t=7630
# Everyone knows the formula for RPKM compuation: rpkm=10^9*C/NL，where C is the reads number of the transcript, L is the length of the transcript and N is the total reads number of the sample
for contig in length_contigs:
	if length_contigs[contig] >= 100 and count_contigs[contig] > 0:
		#rpkm = (10**9)*(count_contigs[contig]/(count*length_contigs[contig]))
		#rpkm_int = count_contigs[contig]/(count*length_contigs[contig])
		rpkm_float = float((10**9)*count_contigs[contig]) / float(float(count)*float(length_contigs[contig]))
		#print "--------------"
		#print "contig: " + contig
		#print "count_contigs[contig]: " + str(count_contigs[contig])
		#print "length_contigs[contig]: " + str(length_contigs[contig])
		#print "count*length_contigs[contig]: " + str(count*length_contigs[contig])
		#print "rpkm_int: " + str(rpkm_int)
		#print "rpkm_float: " + str(rpkm_float)
		print contig + "\t" + str(rpkm_float)
