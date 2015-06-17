#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N tophat.index
#PBS -o tophat.index.out
#PBS -e tophat.index.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2

bowtie2-build Oncorhynchus_mykiss_chr.fa genome_chr_b2.ref


#tophat -G Oncorhynchus_mykiss_chr_annot.gff -p 8 genome_chr_b2.ref s27recov.s27b9n6_R1.paired.fastq.gz,s27recov.s27b9n6_R2.paired.fastq.gz,s27recov.s27b11n2_R1.paired.fastq.gz,s27recov.s27b11n2_R2.paired.fastq.gz,s27recov.s27b7n4_R1.paired.fastq.gz,s27recov.s27b7n4_R2.paired.fastq.gz,s27def.s27b3n6_R1.paired.fastq.gz,s27def.s27b3n6_R2.paired.fastq.gz,s27def.s27b1n7_R1.paired.fastq.gz,s27def.s27b1n7_R2.paired.fastq.gz,s27def.s27b1n2_R1.paired.fastq.gz,s27def.s27b1n2_R2.paired.fastq.gz
