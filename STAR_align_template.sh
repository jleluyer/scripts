#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N STAR_align__BASE__
#PBS -o STAR_align__BASE__.out
#PBS -e STAR_align__BASE__.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/blat/36
module load mugqic/star/2.4.0k

base=__BASE__

STAR --runThreadN 8 \
	--genomeDir /home/leluyer/genomeDirChr \
	--readFilesIn /home/leluyer/"$base"R1.paired.fastq.gz /home/leluyer/"$base"R2.paired.fastq.gz \
	--readFilesCommand zcat \
	--sjdbGTFfile /home/leluyer/Oncorhynchus_mykiss_chr_annot.gff \
	--outFileNamePrefix STAR_alignChr_"$base"
# -l feature='48g
#--genomeChrBinNbits 14 \
	#--limitGenomeGenerateRAM 20000000000
#--sjdbGTFfile /home/leluyer/Oncorhynchus_mykiss_chr_annot.gff \

