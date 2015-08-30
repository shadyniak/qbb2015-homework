#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)

line_count = 0 
total_count = 0 

for line in f:
    if "@" in line:    
        pass
    else:
        column = line.split()
        total_count += int(column[4])
        line_count += 1 

print total_count/line_count
        