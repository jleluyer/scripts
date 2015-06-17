#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N HTseq-countmRNA__BASE__
#PBS -o HTseq-countmRNA__BASE__.out
#PBS -e HTseq-countmRNA__BASE__.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n


module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/tophat/2.0.14
module load mugqic/bowtie2/2.2.5
module load mugqic/samtools/1.2

base=__BASE__

# J'utilise -s no pour no stranded -t pour sortir la feature mRNA et -i pour avoir le id_gene. Idéalement utiliser les exons, mais poru le genome de la truite la nomenclature est différente

#HTSeq-count pour STAR
HTSeq-0.6.1/build/scripts-2.7/htseq-count -f bam -s no -t mRNA -i mRNA STAR_"$base"NamesSorted.bam Oncorhynchus_mykiss_chr_annot.gff >> output_mRNA_HTseq-count_STAR_"$base".txt

#HTSeq-count pour TopHat
HTSeq-0.6.1/build/scripts-2.7/htseq-count -f bam -s no -t mRNA -i mRNA tophat_out_"$base"/tophat_"$base"NamesSorted.bam Oncorhynchus_mykiss_chr_annot.gff >> output_mRNA_tophat_HTseq-count_"$base".txt
