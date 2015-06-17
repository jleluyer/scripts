#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N samtoolsIndex__BASE__
#PBS -o samtoolsIndex__BASE__.out
#PBS -e samtoolIndex__BASE__.err
#PBS -l walltime=01:20:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/igvtools/2.3.49

igvtools [command] [options][arguments]
