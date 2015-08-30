#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/genomes/mappedreads.sam"

f = open(filename)

dictionary = {"2L":0}

for data in f:
    if "@" in data:
        pass 
    else:
        fields = data.split()
        if (str(fields[2]) in dictionary and str(fields[2] > 10000 and str(fields[2]))):
            dictionary[str(fields[2])] += 1 
for key, value in dictionary.iteritems():
    print key, value  