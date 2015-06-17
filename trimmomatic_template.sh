#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N trimmomatic
#PBS -o trimmomatic.out
#PBS -e trimmomatic.err
#PBS -l walltime=01:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8
module load apps/mugqic_pipeline/1.2
module load mugqic/java/jdk1.7.0_60
module load mugqic/trimmomatic/0.32

base=/home/leluyer/HI.1069.007.Index_9.s27b11n2_

java -XX:ParallelGCThreads=1 -Xmx22G -cp $TRIMMOMATIC_JAR org.usadellab.trimmomatic.TrimmomaticPE \
        -phred33 \
        "$base"R1.fastq.gz \
        "$base"R2.fastq.gz \
        "$base"R1.paired.fastq.gz \
        "$base"R1.single.fastq.gz \
        "$base"R2.paired.fastq.gz \
        "$base"R2.single.fastq.gz \
        ILLUMINACLIP:/home/leluyer/univec_trimmomatic.fasta:2:20:7 \
        LEADING:20 \
        TRAILING:20 \
        SLIDINGWINDOW:30:30 \
        MINLEN:60
