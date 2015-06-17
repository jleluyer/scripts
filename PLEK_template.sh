#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N PLEK
#PBS -o PLEK.out
#PBS -e PLEK.err
#PBS -l walltime=01:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load apps/mugqic_pipeline/1.4

python /home/leluyer/PLEK.1.2/PLEK.py -fasta /home/leluyer/assembly_review/Trinity.fasta -out output_PLEK.txt -thread 8 -minlength 300

