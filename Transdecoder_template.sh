#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N transdecoder
#PBS -o transdecoder.out
#PBS -e transdecoder.err
#PBS -l walltime=00:20:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/emboss/6.6.0

/home/leluyer/TransDecoder-2.0.1/TransDecoder.LongOrfs -t DE_def_recov.fasta
