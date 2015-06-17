#!/bin/bash

# De novo assembly Newbler 2.6

/home/leyjer01/454/bin/runAssembly -cdna -urt -o Assembly_cdna_sept_trim -tr  reads_qualtrim.fq 

/home/leyjer01/454/bin/runAssembly -cdna -urt -o Assembly_cdna_sept_notrim -notrim  reads_qualtrim.fq 

#create .sqn file for TSA
/home/leyjer01/tbl2asn -t /home/leyjer01/template.sbt -p . -a s -V v -j "[organism=Oncorhynchus mykiss]"

