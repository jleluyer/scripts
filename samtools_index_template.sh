#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N samtoolsIndex__BASE__
#PBS -o samtoolsIndex__BASE__.out
#PBS -e samtoolIndex__BASE__.err
#PBS -l walltime=01:20:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2

samtools index tophat_ALL/accepted_hits.bam
