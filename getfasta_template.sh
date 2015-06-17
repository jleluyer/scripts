#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N getfasta
#PBS -o getfasta.out
#PBS -e getfasta.err
#PBS -l walltime=00:20:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

#/home/leluyer/get_fasta_alignedContig.py /home/leluyer/list_TEMP_DE_def_recov.txt /home/leluyer/assembly_review/Trinity.fasta > DE_def_recov.fasta

/home/leluyer/get_fasta_alignedContig.py /home/leluyer/list_align_mrna_DE_def_recov.txt /home/leluyer/Oncorhynchus_mykiss_mrna.fa > genome_mrna_DE_def_recov.fasta
