#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N blastx_
#PBS -o blastx.out
#PBS -e blastx.err
#PBS -l walltime=00:40:00
#PBS -l nodes=1:ppn=8
#PBS -r n


cat genome_mrna_DE_def_recov.fasta | parallel -j 8 -k --block 10k --recstart '>' --pipe blastx -db /home/leluyer/454/dbs/uniprot/uniprot_sprot.fasta  -query - -outfmt 6 -max_target_seqs 1 -evalue 1e-6 > blastx_genome_DEdef_recov_sprot.txt
