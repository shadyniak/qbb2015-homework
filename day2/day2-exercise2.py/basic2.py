#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)

perfect_alignment = 0 

#NM:i:0 is for no bases off 
#NM:i:1 is for one mismatch 
#XN:i:1 is for ambigugous 

for alignment in f:
    if "NM:i:0" in alignment:
            perfect_alignment += 1
    else:
        pass 
        
print perfect_alignment 

