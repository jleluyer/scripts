#!/bin/bash

# used to map the transcriptome on the genome with a splice-tolerant aligner 

# Global variables
file="transcriptome.fasta"
GENOMEFOLDER="/genome/directory/"
GENOME="genome_gmap_format"


# prepare the reference
gmap_build --dir=/genome/directory/ /genome/directory/genome.fasta -d genome_gmap_format

# Align reads
cat "$file"| gmap -t 8 --dir="$GENOMEFOLDER" -d "$GENOME" -f gff3_gene --gff3-add-separators=0 >transcriptome_annotation.gff3
