#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N blat_DE
#PBS -o blat_DE.out
#PBS -e blat_DE.err
#PBS -l walltime=00:30:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -m ea 
#PBS -l nodes=1:ppn=8
#PBS -r n

module load compilers/gcc/4.8  apps/mugqic_pipeline/2.1.1
module load mugqic/blat/36

blat /home/leluyer/Oncorhynchus_mykiss_mrna.fa /home/leluyer/DE_def_recov.fasta output_blat_mrna.psl

blat /home/leluyer/Oncorhynchus_mykiss_chr.fa /home/leluyer/DE_def_recov.fasta output_blat_chr.psl


#blat database query [-ooc=11.ooc] output.psl
#	-t=type        Database type.  Type is one of:
#                    dna - DNA sequence
#                    prot - protein sequence
#                    dnax - DNA sequence translated in six frames to protein
#                  The default is dna.
#   -q=type        Query type.  Type is one of:
#                    dna - DNA sequence
#                    rna - RNA sequence
#                    prot - protein sequence
#                    dnax - DNA sequence translated in six frames to protein
#                    rnax - DNA sequence translated in three frames to protein
#                  The default is dna.
#   -prot          Synonymous with -t=prot -q=prot.
#   -ooc=N.ooc     Use overused tile file N.ooc.  N should correspond to 
#                  the tileSize.
#   -tileSize=N    Sets the size of match that triggers an alignment.  
#                  Usually between 8 and 12.
#                  Default is 11 for DNA and 5 for protein.
#   -stepSize=N    Spacing between tiles. Default is tileSize.
#   -oneOff=N      If set to 1, this allows one mismatch in tile and still
#                  triggers an alignment.  Default is 0.
#   -minMatch=N    Sets the number of tile matches.  Usually set from 2 to 4.
#                  Default is 2 for nucleotide, 1 for protein.
#   -minScore=N    Sets minimum score.  This is the matches minus the 
#                  mismatches minus some sort of gap penalty.  Default is 30.
#   -minIdentity=N Sets minimum sequence identity (in percent).  Default is
#                  90 for nucleotide searches, 25 for protein or translated
#                  protein searches.
#   -maxGap=N      Sets the size of maximum gap between tiles in a clump.  Usually
#                  set from 0 to 3.  Default is 2. Only relevent for minMatch > 1.
#   -noHead        Suppresses .psl header (so it's just a tab-separated file).
#   -makeOoc=N.ooc Make overused tile file. Target needs to be complete genome.
#   -repMatch=N    Sets the number of repetitions of a tile allowed before
#                  it is marked as overused.  Typically this is 256 for tileSize
#                  12, 1024 for tile size 11, 4096 for tile size 10.
#                  Default is 1024.  Typically comes into play only with makeOoc.
#                  Also affected by stepSize: when stepSize is halved, repMatch is
#                  doubled to compensate.
#   -mask=type     Mask out repeats.  Alignments won't be started in masked region
#                  but may extend through it in nucleotide searches.  Masked areas
#                  are ignored entirely in protein or translated searches. Types are:
#                    lower - mask out lower-cased sequence
#                    upper - mask out upper-cased sequence
#                    out   - mask according to database.out RepeatMasker .out file
#                    file.out - mask database according to RepeatMasker file.out
#   -qMask=type    Mask out repeats in query sequence.  Similar to -mask above, but
#                  for query rather than target sequence.
#   -repeats=type  Type is same as mask types above.  Repeat bases will not be
#                  masked in any way, but matches in repeat areas will be reported
#                  separately from matches in other areas in the psl output.
#   -minRepDivergence=NN   Minimum percent divergence of repeats to allow 
#                  them to be unmasked.  Default is 15.  Only relevant for 
#                  masking using RepeatMasker .out files.
#   -dots=N        Output dot every N sequences to show program's progress.
#   -trimT         Trim leading poly-T.
#   -noTrimA       Don't trim trailing poly-A.
#   -trimHardA     Remove poly-A tail from qSize as well as alignments in 
#                  psl output.
#   -fastMap       Run for fast DNA/DNA remapping - not allowing introns, 
#                  requiring high %ID. Query sizes must not exceed 5000.
#   -out=type      Controls output file format.  Type is one of:
#                    psl - Default.  Tab-separated format, no sequence
#                    pslx - Tab-separated format with sequence
#                    axt - blastz-associated axt format
#                    maf - multiz-associated maf format
#                    sim4 - similar to sim4 format
#                   wublast - similar to wublast format
#                    blast - similar to NCBI blast format
#                    blast8- NCBI blast tabular format
#                    blast9 - NCBI blast tabular format with comments
#   -fine          For high-quality mRNAs, look harder for small initial and
#                  terminal exons.  Not recommended for ESTs.
#   -maxIntron=N  Sets maximum intron size. Default is 750000.
#   -extendThroughN  Allows extension of alignment through large blocks of Ns."

