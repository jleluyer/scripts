#PBS -A bpv-355-aa
#PBS -N transabyss_test
#PBS -o transabyss_test.out
#PBS -e transabyss_test.err
#PBS -l walltime=24:00:00
#PBS -M jeremy.le-luyer.1@ulaval.ca
#PBS -l feature=48g
#PBS -m ea
#PBS -l nodes=1:ppn=8

#PBS -r n
 
module load compilers/gcc/4.8 apps/python/2.7.5 libs/igraph
source $HOME/apps/myvenv/bin/activate
module load apps/mugqic_pipeline/1.4
module load mugqic/ucsc/20141112
pip install wheel


transabyss-1.5.2/transabyss --pe subset_r1_testaa.fastq.fastq subset_r2_testaa.fastq.fastq subset_r1_testab.fastq.fastq subset_r2_testab.fastq.fastq subset_r1_testac.fastq.fastq subset_r2_testac.fastq.fastq subset_r1_testad.fastq.fastq subset_r2_testad.fastq.fastq subset_r1_testae.fastq.fastq subset_r2_testae.fastq.fastq subset_r1_testaf.fastq.fastq subset_r2_testaf.fastq.fastq subset_r1_testag.fastq.fastq subset_r2_testag.fastq.fastq subset_r1_testah.fastq.fastq subset_r2_testah.fastq.fastq subset_r1_testai.fastq.fastq subset_r2_testai.fastq.fastq subset_r1_testaj.fastq.fastq subset_r2_testaj.fastq.fastq subset_r1_testak.fastq.fastq subset_r2_testak.fastq.fastq subset_r1_testal.fastq.fastq subset_r2_testal.fastq.fastq subset_r1_testam.fastq.fastq subset_r2_testam.fastq.fastq subset_r1_testan.fastq.fastq subset_r2_testan.fastq.fastq subset_r1_testao.fastq.fastq subset_r2_testao.fastq.fastq --outdir test_abyss --name test_multifilesinput --threads 8 -k 60 --island 0 --length 100


