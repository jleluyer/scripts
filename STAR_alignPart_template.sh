#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N STAR_alignPart
#PBS -o STAR_alignPart.out
#PBS -e STAR_alignPart.err
#PBS -l walltime=00:20:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/blat/36
module load mugqic/star/2.4.0k

STAR --runThreadN 8 \
	--genomeDir /home/leluyer/genomeChr_10/ \
	--readFilesIn head_s27recov.s27b7n4_R1.paired.fastq head_s27recov.s27b7n4_R2.paired.fastq \
	--sjdbGTFfile /home/leluyer/chr_10_annot.gff \
	--outFileNamePrefix STAR_alignPart_out

#--genomeChrBinNbits 14 \
	#--limitGenomeGenerateRAM 20000000000
#--sjdbGTFfile /home/leluyer/Oncorhynchus_mykiss_chr_annot.gff \

