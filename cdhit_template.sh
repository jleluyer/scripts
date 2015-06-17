#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N CDHIT_test
#PBS -o CDHIT_test.out
#PBS -e CDHIT_test.err
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=8
#PBS -r n
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/cd-hit/4.6.1-2012-08-27

cd-hit-est -i /home/leluyer/trymerge.fa -o /home/leluyer/cdhit_merge_90.fa -c 0.9 -n 8 -T 8
