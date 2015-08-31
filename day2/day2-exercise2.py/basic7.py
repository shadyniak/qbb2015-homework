#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)

dictionary = {"2L":0}

for data in f:
    if "@" in data:
        pass 
    else:
        fields = data.split()
        gene_name = fields[2]
        start = fields[3]
        start.lstrip(("LN:"))
        start = int(start)
        if ((str(fields[2]) in dictionary) and 10000 < start < 20000):
            dictionary[str(fields[2])] += 1 
for key, value in dictionary.iteritems():
    print key, value  