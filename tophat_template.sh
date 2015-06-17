#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N tophat__BASE__
#PBS -o tophat__BASE__.out
#PBS -e tophat__BASE__.err
#PBS -l walltime=48:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

#base=__BASE__

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2

#bowtie2-build subset_genome.fa genome_subset_b2.ref


tophat -o tophat_ALL -G /home/leluyer/Oncorhynchus_mykiss_chr_annot.gff -p 8 /home/leluyer/genome_chr_b2.ref /home/leluyer/assembly_review/all_r1.fasta /home/leluyer/assembly_review/all_r2.fasta
