#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N getorf
#PBS -o getorf.out
#PBS -e getorf.err
#PBS -l walltime=10:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/emboss/6.6.0

#getorf -sequence DE_def_recov.fasta -outseq orf_DE_def_recov.fasta -minsize 300

getorf -sequence DE_def_recov.fasta -find 4 -outseq orf_DE_def_recov_find4.fasta -minsize 300
