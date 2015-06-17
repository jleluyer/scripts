#!/bin/bash

i=HI.1118.001.Index_22.s27b9n1_
        java -Xmx30G -jar /is1/commonPrograms/Trimmomatic-0.30/trimmomatic-0.30.jar PE \
            -threads 9 \
            -phred33 \
            "$i"R1.fastq.gz \
            "$i"R2.fastq.gz \
            "$i"R1.paired.fastq.gz \
            "$i"R1.single.fastq.gz \
            "$i"R2.paired.fastq.gz \
            "$i"R2.single.fastq.gz \
            ILLUMINACLIP:univec_trimmomatic.fasta:2:20:7 \
            LEADING:20 \
            TRAILING:20 \
            SLIDINGWINDOW:30:30 \
            MINLEN:60
