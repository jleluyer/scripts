#!/bin/bash


/home/leyjer01/run_text.pl \
			--left /is1/users/leyjer01/RNADataTest/Data_JLL/rna_seq_review/all_r1.fastq \
                        --right /is1/users/leyjer01/RNADataTest/Data_JLL/rna_seq_review/all_r2.fastq \
                        --genome /is1/users/leyjer01/genome/chr/Oncorhynchus_mykiss_chr.fa \
                        --seqType fq \
                        --SS_lib_type RF \
                        -I 1000 \
                        --trim_short_terminal_segments 10 \
                        -P 97 -C 1 -o output_chr_blat.dir
