#!/usr/bin/env python 

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

import sys

#open using arguments 

#print sys.argv
#filename = sys.argv[1]

#f = open(filename)

f = sys.stdin #how to oepn: /Users/cmdb/qbb2015/day3 $ cat /Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab | ./filter.py | head
# also /Users/cmdb/qbb2015/day3 $ cat /Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab | grep CG | ./filter.py | head
# also ./filter.py < /Users/cmdb/qbb2015/day3 $ cat /Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab

#you could use a loop 
# for filename in sys.argv[1:6]: 
#indent everything after 

name_counts = {}

#Iterate the file line by line
for line_count, data in enumerate(f):
    fields = data.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
            name_counts [gene_name] = 1 
    else:
        name_counts[gene_name] += 1
        
# Iterate key, value pairs from the name counts dictionary 
for key, value in name_counts.iteritems():
    print key, value 
    
     
        