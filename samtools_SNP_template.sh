#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N samtoolsSNP__BASE__
#PBS -o samtoolsSNP__BASE__.out
#PBS -e samtools_SNP__BASE__.err
#PBS -l walltime=00:10:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2


#samtools faidx chr10.fa

#samtools mpileup -g -f /home/leluyer/chr10.fa tophat_subset_sample1_/accepted_hits.bam tophat_subset_sample2_/accepted_hits.bam > var.raw.bcf

bcftools view var.raw.bcf | vcfutils.pl varFilter -D100 > var.flt.vcf

