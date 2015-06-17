#!/bin/bash

#assembly with trinity

./Trinity.pl --min_contig_length 100 --seqType fq --JM 10G  --single reads/reads_cut_e0.2_n3_18_miracleans.fastq --CPU 6
