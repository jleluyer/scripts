#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N fastqc__BASE__
#PBS -o fastqc__BASE__.out
#PBS -e fastqc__BASE__.err
#PBS -l walltime=01:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8
module load apps/mugqic_pipeline/1.2
module load mugqic/java/jdk1.7.0_60
module load mugqic/fastqc/0.11.2

base=/home/leluyer/trinity/H2/transcriptome_review.dir/HI.1072.008.Index_19.P60_R1.paired.fastq.gz

mkdir "$base".dir

fastqc -o "$base".dir -f fastq "$base"

