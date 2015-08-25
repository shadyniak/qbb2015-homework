#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)

one_alignment = 0 

for alignment in f:
    if "NH:i:1" in alignment:
            one_alignment += 1
    else:
        pass 
        
print one_alignment 
