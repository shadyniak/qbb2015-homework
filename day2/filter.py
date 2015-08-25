#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open(filename)

for data in f:
    fields = data.split()
    if "tRNA" in fields[9]:
        print data, ### the comma supresses the new line that is automatically generated with print