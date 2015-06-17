#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N samtoolsSortSTAR__BASE__
#PBS -o samtoolsSortSTAR__BASE__.out
#PBS -e samtoolsSortSTAR__BASE__.err
#PBS -l walltime=06:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2

base=__BASE__


samtools view -bS STAR_alignChr_"$base"Aligned.out.sam | samtools sort -n - STAR_alignChr_"$base"CoordSorted

#alternative
#samtools view -bS sample1.sam > sample1
#samtools sort sample1.bam sample1_sorted.bam
