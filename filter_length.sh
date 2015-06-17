#!/bin/bash

awk '!/^>/ { next } { getline seq } length(seq) >= 200 { print $0 "\n" seq }' merge_assembly.fa > merge_assembly.ge200.fa
