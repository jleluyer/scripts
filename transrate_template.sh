#!/bin/bash

#PBS -A bpv-355-aa
#PBS -N transrate_protref
#PBS -o transrate_protref.out
#PBS -e transrate_protref.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/blast/2.2.30+

transrate --assembly /home/leluyer/assembly_review/Trinity.fasta \
	--reference /home/leluyer/Oncorhynchus_mykiss_pep.fa \
	--threads 8
