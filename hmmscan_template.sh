#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N hmmscan
#PBS -o hmmscan.out
#PBS -e hmmscan.err
#PBS -l walltime=00:30:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/emboss/6.6.0

# usage extract pfam database,  hmmpress makes necesaries db installation, hmmscan search #

#gunzip Pfam-A.hmm.gz

#/home/leluyer/hmmer-3.1b2-macosx-intel/src/hmmpress Pfam-A.hmm

#/home/leluyer/hmmer-3.1b2-macosx-intel/src/hmmscan -E 0.00001 --cpu 8 --tblout PfamScan_300.out --domtblout Pfscan_300.domout -o output_300_pfam Pfam-A.hmm orf_DE_def_recov.fasta

/home/leluyer/hmmer-3.1b2-macosx-intel/src/hmmscan --cpu 8 --domtblout pfam_transcoder.domtblout /home/leluyer/Pfam-A.hmm DE_def_recov.fasta.transdecoder_dir/longest_orfs.pep
