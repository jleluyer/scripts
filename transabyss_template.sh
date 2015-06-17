#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N transabyss
#PBS -o transabyss.out
#PBS -e transabyss.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -l feature=48g
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


#need to compile (./configure && make) abyss-1.5.2 and transabyss-1.5.2 on conpiler gcc
#need to download (wget http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.bz2) and decompress (tar jxf boost_1_55_0.tar.bz2) in abyss-1.5.2 prior to configure abyss
#use blat 35x1

module load compilers/gcc/4.8 apps/python/2.7.5 libs/igraph
source $HOME/apps/myvenv/bin/activate
module load apps/mugqic_pipeline/1.4
module load mugqic/ucsc/20141112
pip install wheel


transabyss-1.5.2/transabyss --pe all_r1.fastq.gz all_r2.fastq.gz --outdir test_assembly_abyss_60k --name assembly_60k --threads 8 -k 60 --island 0 --length 100

