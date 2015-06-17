#!/bin/bash
#PBS -A bpv-355-aa
#PBS -N output_butterfly_commands_ab
#PBS -o output_butterfly_commands_ab.out
#PBS -e output_butterfly_commands_ab.err
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=8
#PBS -r n

module load java/jdk1.6.0
module load apps/bowtie/1.0.0-1
module load apps/samtools/0.1.19-1



#cat /rap/bpv-355-aa/trinityrnaseq_r2013_08_14/trinity_out_dir_2013-12-05/chrysalis/butterfly_commands_ab|parallel -j 8

#sed -i 's#\/is1\/users\/leyjer01\/454_OncMyk\/Trinity\/trinityrnaseq_r2012-10-05\/#\/rap\/bpv-355-aa\/trinityrnaseq_r2013_08_14\/#g' /rap/bpv-355-aa/trinityrnaseq_r2013_08_14/test_assembly_2/chrysalis/butterfly_commands

cat /rap/bpv-355-aa/trinityrnaseq_r2013_08_14/trinity_out_dir_2013-12-05/chrysalis/butterfly_commands_ab|parallel -j 8

#find /rap/bpv-355-aa/trinityrnaseq_r2013_08_14/test_assembly_2/ -name "*allProbPaths.fasta" -exec cat {} + > /rap/bpv-355-aa/trinityrnaseq_r2013_08_14/test_assembly_2/Trinity.fasta
