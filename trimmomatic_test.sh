#!/bin/bash

i=__BASE__
        java -Xmx30G -jar /is1/commonPrograms/Trimmomatic-0.30/trimmomatic-0.30.jar PE \
            -threads 9 \
            -phred33 \
            "$i"_R1.fastq.gz \
            "$i"_R2.fastq.gz \
            "$i"_R1.paired.fastq.gz \
            "$i"_R1.single.fastq.gz \
            "$i"_R2.paired.fastq.gz \
            "$i"_R2.single.fastq.gz \
            ILLUMINACLIP:univec_trimmomatic.fasta:2:20:7 \
            LEADING:20 \
            TRAILING:20 \
            SLIDINGWINDOW:30:30 \
            MINLEN:60
