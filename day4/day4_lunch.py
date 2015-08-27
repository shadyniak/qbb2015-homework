#!/usr/bin/env python

""""
For the insulator proteins CTCF, BEAF, and Su(HW), determine:

How many regions are bound each protein alone
How many are bound by two proteins
How many are bound by three proteins
Summarize these results in a venn diagram

"""

from __future__ import division 
import numpy as np 
import sys
import copy 
import matplotlib.pyplot as plt 
from matplotlib_venn import venn3, venn3_circles


def arrays_from_len_file(fname): #we can give it a file 
    arrays = {} #create a dictionary as an array 
    for line in open(fname):
        fields = line.split() #split columns 
        name = fields[0] 
        size = int(fields[1]) #reading in the size of the chromosome as an integer, and then we will read it in as 0's 
        arrays[name] = np.zeros(size, dtype=bool) #name say we're storing everything in arrays as a key 'name' #we only need to store one type of information, did we have hit on out target - boolean  
    return arrays 
    
def set_bits_from_file(arrays, fname):
    for line in open(fname):
        fields = line.split()
        #we need the total length of the transcript (start and end) and chromosome name
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[chrom][start:end] = 1 #creates a bool array for a chromosome and looking up the start to end slice, fill with 1's 

#import files in this order!!!!!!!!!!!!!!
    
arrB = arrays_from_len_file(sys.argv[1])
arrC = arrays_from_len_file(sys.argv[1])
arrS = arrays_from_len_file(sys.argv[1]) #1 is the genome 
BEAF = set_bits_from_file(arrB, sys.argv[2])#the first .bed file 
CTCF = set_bits_from_file(arrC, sys.argv[3])
SuHW = set_bits_from_file(arrS, sys.argv[4])

#NEED SEVEN COMPARISONS BETWEEN LEN, BEAF, CTCF, AND SUHW

count1 = 0 
count2 = 0 
count3 = 0 
count4 = 0 
count5 = 0 
count6 = 0 
count7 = 0 
total = 0 

for filename in sys.argv[2:]:
    for line in open(filename):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        #get slice 
        sl1 = arrB[chrom][start:end]
        sl2 = arrC[chrom][start:end]
        sl3 = arrS[chrom][start:end]
        
        if sl1.all() & sl2.all() & sl3.all():
            count7 += 1
        elif sl1.all() & sl2.all() &~ sl3.all():
            count6 += 1 
        elif sl1.all() &~ sl2.all() & sl3.all():
            count5 += 1
        elif sl3.all() & sl2.all() &~ sl1.all():
            count4 += 1
        elif sl1.all() &~ sl2.all() &~ sl3.all():
            count3 += 1
        elif sl3.all() &~ sl2.all() &~ sl1.all():
            count2 += 1
        else:
            count1 += 1 

plt.figure()
venn3(subsets=(count1, count2, count3, count4, count5, count6, count7), set_labels = ('BEAF', 'CTCF', 'SuHW'))
plt.savefig("Venn.png")
