#!/bin/bash

#PBS -A bpv-355-aa
#PBS -N transrate_comp
#PBS -o transrate_comp.out
#PBS -e transrate_comp.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/blast/2.2.30+

transrate --assembly /home/leluyer/assembly_review/Trinity.fasta,/home/leluyer/raw_data/assembly_dec_test.Trinity.fasta,/home/leluyer/trinity/H3/genome_guided.dir/genome_guided_trinity/trinity_genomeGuided.dir/Trinity-GG_modifHeader.fasta \
	--threads 8
