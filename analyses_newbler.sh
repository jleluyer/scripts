#!/bin/bash

####

#script for downstream analysis de novo Assembly with newbler

####


#blast Uniprot
blastx -db /is1/users/leyjer01/454_OncMyk/db/uniprot/uniprot_sprot.fasta -query 454Isotigs100.fna -outfmt 6 -num_threads 36 -max_target_seqs 1 -evalue 1e-08 -out blast_newbler_uniprot.out

# blast est
blastn -db /is1/users/leyjer01/454_OncMyk/db/est_Trout/estTrout -query 454Isotigs100.fna -outfmt 6 -evalue 1e-08 -max_target_seqs 1 -num_threads 36 -out blast_newbler_est.out

# blast Nr
blastx -db /is1/commonDatasets/nr-20121220/nr -query /454Isotigs100.fna -evalue 1e-08 -num_threads 36 -out blast_newbler_nr.out

# blast Nr
blastx -db /is1/commonDatasets/nr-20121220/nr -query /454Isotigs100.fna -outfmt 6 -max_target_seqs 1 -evalue 1e-08 -num_threads 36 -out blast_newbler_nr_6.out

##statistics
grep '>' 454Isotigs100.fna|cut -f 4|awk '{print $3}'|sed 's/length=//g' > length_isotigs100.txtgrep '>' 454Isotigs100.fasta|awk '{print $2}'|sed 's/len=//g' > length_trinity_transcripts.txt

#mean length
awk '{ total += $1 } END { print total/NR }' length_newbler_isotigs100.txt

#blastx statistics
cat blast_newbler_uniprot.out blast_trinity_uniprot.out > blast_cat_uniprot.txt

# check identical entries
awk '{print $2}' blast_cat_uniprot.txt|sed 's/|/ /g'|sed 's/_/ /g'|awk '{print $2}'|sort|uniq > uniprot_entries.txt

# check percent of identical species
awk '{print $2}' blast_cat_uniprot.txt|sed 's/|/ /g'|sed 's/_/ /g'|awk '{print $4}'|sort|uniq -c|sort -g > uniprot_species.txt

# make reference index for bwa
/is1/commonPrograms/bwa-0.7.5a/bwa index 454Isotigs100.fasta

#align all reads to transcriptome
/is1/commonPrograms/bwa-0.7.5a/bwa mem -t 12 454Isotigs100.fna /is1/users/leyjer01/454_OncMyk/Newbler/reads/reads_qualtrim_all.fq > newbler_all.sam

#calculate RPKM
/home/leyjer01/calculateRPKM.py 454Isotigs100.fna newbler_all.sam > rpkm_newbler.txt 

#mean coverage all isotigs 100 bp
awk '{ total += $2 } END { print total/NR }' bwa/rpkm_newbler.txt

#get orfs all non annotated seequences
 /is1/commonPrograms/EMBOSS-6.5.7/emboss/getorf -sequence non_annotated_sequences.fna -minsize 90 -outseq orfs/orf_30bp_non_annotated.fna

# count orfs with large orfs > 100
 /is1/commonPrograms/EMBOSS-6.5.7/emboss/getorf -sequence annotated_novel_sequences.fna -minsize 300 -outseq orfs/orf_100bp_annotated.fna

grep '>' orf_100bp_annotated.fna|awk '{print $1}'|sed 's/_/ /g'|awk '{$NF = ""; print}'|sed 's/ /_/g'|sort|uniq|wc -l

grep '>' orf_100bp_annotated.fna|awk '{print $1}'|sed 's/_/ /g'|awk '{$NF = ""; print}'|sed 's/ /_/g'|sort|uniq > orf_annotated_novel_sequences_100.txt

sed -ie 's/_$//' orf_annotated_novel_sequences_100.txt
#blastp orfs non annotated sequences
blastp -db /is1/users/leyjer01/454_OncMyk/db/uniprot/uniprot_sprot.fasta -query orfs/orf_30bp_non_annotated.fna -outfmt 6 -max_target_seqs 1 -evalue 1e-08 -num_threads 12 -out blastp_orfs_non_annotated.out

#calcul N50
grep "^>" 454Isotigs100.fna | cut -d"=" -f2 | cut -d" " -f1 | ./stdin_N50.py 

#calcule size and quality of fasta sequence
awk '{if(NR%4==2) print length($0)}' file.fastq > readLength

awk '{if(NR%4==0) print NR"\t"$0"\t"length($0)}' file.fastq > qualityLength

#get length sequence fasta
awk '{/>/&&++a||b+=length()}END{print b/a}' ../Trinity.fasta

#get sequences larger than
grep '>' assembly_review/Trinity_1902.fasta|sed 's/len=//g'|awk '$2 > 1000 {print $2}'|wc -l

#remove duplicate first column based on third column value
awk '{ if (!($1 in a)) a[$1] = $3; else if (a[$1] < $3) a[$1] = $3 } END { for (key in a) print key, a[key] }' essai.txt
