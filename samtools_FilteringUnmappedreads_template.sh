


samtools view -h -F 4 blah.bam > blah_only_mapped.sam
OR
samtools view -h -F 4 -b blah.bam > blah_only_mapped.bam
