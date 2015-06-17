#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N samstat_TEMP
#PBS -o samstat_TEMP.out
#PBS -e samstat_TEMP.err
#PBS -l walltime=03:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load apps/samtools/1.0


/home/leluyer/samstat-1.5/src/samstat tophat_out_s27norm.s27b3n8_/accepted_hits.bam


