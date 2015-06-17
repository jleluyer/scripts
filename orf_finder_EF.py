#!/usr/bin/python
# encoding: utf-8
# Adapted from Eric Paquet's NTRidentification.py script.
# Outputs protein translations for unidentified contigs.

import sys,pdb
from Bio import SeqIO
import Bio
from Bio.Seq import Seq

def translation(seq):
    transArray = str(Bio.Seq.translate(seq)).split("*")
    sortedTransArray = sorted(transArray, key = lambda trans:-len(trans))
    return sortedTransArray[0]
#    return Seq(str(Bio.Seq.translate(seq)).split("*")[0])

def sixFramesTranslation(biopythonDNAseq):
    sixFtrans=[]
    sixFtrans.append(translation(biopythonDNAseq[0::])) # + 1
    sixFtrans.append(translation(biopythonDNAseq[1::])) # + 2
    sixFtrans.append(translation(biopythonDNAseq[2::])) # + 3
    reverseComplement=biopythonDNAseq.reverse_complement()
    sixFtrans.append(translation(reverseComplement[0::])) # - 1
    sixFtrans.append(translation(reverseComplement[1::])) # - 2
    sixFtrans.append(translation(reverseComplement[2::])) # - 3
    return sixFtrans

def main():
    # Read the fasta file and place sequences in a dictionary contigSequences
    # indexed by sequence names
    contigList=list(SeqIO.parse(open(sys.argv[1]), "fasta"))
    protOut=open(sys.argv[2], "w")
    for contig in contigList:
        proteinSequences=sixFramesTranslation(contig.seq)
        significantSequences=filter(lambda a:len(a) >= 30, proteinSequences)
        i=0;
        for sequence in significantSequences:
            print >>protOut,">%s_%d\n%s"%(contig.name,i,str(sequence))
            i=i+1
    protOut.close()

if __name__ == "__main__":
    main()
        



