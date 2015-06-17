#!/bin/bash

########
#script for reads 454 preprocessing from both .fna and .qual files. Still to improve steps (e.g extract directly wanted ids to .fastq file)
########



#####cat reads

cat HP0KBV1.RL12.fna HP344L0.RL12.fna HPNPAWQ.RL12.fna > reads.fna

cat HP0KBV1.RL12.qual HP344L0.RL12.qual HPNPAWQ.RL12.qual > reads.qual

### combine fasta et .qual to fastq

perl /home/leyjer01/fasta_qual_to_fastq.pl reads.fna reads.qual > reads.fq

##Check data 1st time

#mkdir outputfastqc
/home/leyjer01/FastQC/fastqc -f fastq reads.fq -t 12 -o outputfastqc


#reverse complement file to improve cutadapt step
#is1/commonPrograms/fastx_toolkit-0.0.13.2/src/fastx_reverse_complement/fastx_reverse_complement -i "input sequence" -o "output sequence"

# cutadapt
/is1/commonPrograms/cutadapt-1.2.1/bin/cutadapt $(<cutadapt_454_all_rc.conf) -n 3 reads.fq -o reads_cut.fq

# MIRA
/is1/commonPrograms/mira_4.0rc1_linux-gnu_x86_64_static/bin/mirabait -f fastq -t fastq -k 18 -i /home/leyjer01/454/bin/Univec.fasta reads_cut.fq  reads_mira

# quality and minimum length trimming
/is1/commonPrograms/fastx_toolkit-0.0.13.2/src/fastq_quality_filter/fastq_quality_trimmer -Q33 -t 20 -l 50 -i reads_mira.fastq -o reads_qualtrim.fq 

