#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N STAR_indexPart
#PBS -o STAR_indexPart.out
#PBS -e STAR_indexPart.err
#PBS -l walltime=00:20:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/blat/36
module load mugqic/star/2.4.0k

ulimit -c unlimited

STAR --runThreadN 1 \
	--runMode genomeGenerate \
	--genomeDir /home/leluyer/genomeChr_10 \
	--genomeFastaFiles /home/leluyer/chr_10.fa \
	--sjdbOverhang 99 \
	--genomeChrBinNbits 10 \
	--limitGenomeGenerateRAM 20000000000

#--sjdbGTFfile /home/leluyer/chr10_annot.gff \
	#--sjdbGTFfile /home/leluyer/chr1_annot.gff \
	#--limitGenomeGenerateRAM 15000000000
	#--sjdbGTFfile /home/leluyer/Oncorhynchus_mykiss_chr_annot.gff \
#       --genomeChrBinNbits 14 \
