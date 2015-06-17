#!/bin/bash



blastn -db -query /is1/users/leyjer01/454_OncMyk/Trinity/trinityrnaseq_r2013-02-25/trinity_out_dir/Trinity.fasta -num_threads 36 -max_target_seqs 1 -outfmt 6 -out blast_trinity_est.out

# standard blast nr

blastx -db /is1/commonDatasets/nr-20121220/nr -query /is1/users/leyjer01/454_OncMyk/Trinity/trinityrnaseq_r2013-02-25/trinity_out_dir/Trinity.fasta-evalue 1e-08 -num_threads 36 -out blast_trinity_nr.out
















# mkae reference index for Trinity
/is1/commonPrograms/bwa-0.7.5a/bwa index Trinity.fasta

#align all trimmed reads on trinity.fasta
/is1/commonPrograms/bwa-0.7.5a/bwa mem -t 12 Trinity.fasta  /is1/users/leyjer01/454_OncMyk/Newbler/reads/reads_qualtrim_all.fq > trinity_all.sam

#Align reads to trasncriptome
/home/leyjer01/calculateRPKM.py Trinity.fasta trinity_all.sam > rpkm_trinity.txt  
