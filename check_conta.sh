!/bin/bash


# download Univec databse (je t'ai mis le lien pour un fichier de vecteurs, adaptateurs, etc... qui peut être utile)

wget ftp://ftp.ncbi.nih.gov/pub/UniVec/UniVec
mv UniVec univec.fasta

# make database index

makeblastdb -in univec.fasta -dbtype nucl

# blast your data on indexs files

blastn -task blastn-short -db univec.fasta -query <your.file.fasta> -max_target_seqs 1 -outfmt 6 -num_threads 12 -out check_conta.out &

