#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N samstat_try
#PBS -o samstat.out
#PBS -e samstat.err
#PBS -l walltime=00:30:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load apps/samtools/1.0


samtools view -bh essai_cds+utr_s18b9n3.sam > out_essai_cds+utr_s18b9n3.bam
