#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N tophat__BASE__
#PBS -o tophat__BASE__.out
#PBS -e tophat__BASE__.err
#PBS -l walltime=00:05:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

base=__BASE__

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2
module load apps/samtools/1.0

bowtie2-build chr10.fa chr10_b2.ref


#tophat -o tophat_out_"$base" -G chr10_annot.gff -p 8 genome_chr_b2.ref "$base"R1.paired.fastq.gz "$base"R2.paired.fastq.gz
