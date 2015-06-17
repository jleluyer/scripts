#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N bwa_try
#PBS -o bwa.out
#PBS -e bwa.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n



module load compilers/gcc/4.8
module load apps/mugqic_pipeline/1.4 
module load apps/bwa/0.7.5a



#bwa index -a bwtsw /home/leluyer/Oncorhynchus_mykiss_chr.fa -p output_chr_bwa

bwa mem -t 8 output_chr_bwa /home/leluyer/trinity/H3/transcriptome_review_cdhit.dir/HI.1010.008.h3_s18_norm_Index_8.s18b9n3_R1.paired.fastq.gz /home/leluyer/trinity/H3/transcriptome_review_cdhit.dir/HI.1010.008.h3_s18_norm_Index_8.s18b9n3_R2.paired.fastq.gz > essai_chr_s18b9n3.sam
