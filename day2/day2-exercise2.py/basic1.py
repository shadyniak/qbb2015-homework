#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)

line_count = 0 

for line in f:
    if "@" in line:
        pass
    else:
        line_count += 1 
print line_count 
        