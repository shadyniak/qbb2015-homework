#!/usr/bin/env python

from __future__ import division
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import sys 
import chrombits
    
arr=chrombits.ChromosomeLocationBitArrays(fname=sys.argv[1])

ctcf = arr.copy()
beaf = arr.copy()
suhw = arr.copy()

ctcf.set_bits_from_file(sys.argv[2])
beaf.set_bits_from_file(sys.argv[3])
suhw.set_bits_from_file(sys.argv[4])

union = beaf.union(ctcf.union(suhw))


convertedunion=union.bed()


count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0


for chrom, start, end in convertedunion:
    sl1 = ctcf.arrays[chrom][start:end]
    sl2 = beaf.arrays[chrom][start:end]
    sl3 = suhw.arrays[chrom][start:end]
       
    if sl1.any() and sl2.any() and sl3.any():
        count7 += 1
    elif sl1.any() and sl2.any() and not sl3.any():
        count6 += 1
    elif sl1.any() and not sl2.any() and sl3.any():
        count5 += 1
    elif sl3.any() and sl2.any() and not sl1.any():
        count4 += 1
    elif sl1.any() and not sl2.any() and not sl3.any():
        count3 += 1
    elif sl3.any() and not sl2.any() and not sl1.any():
        count2 += 1
    else:
        count1+=1
        
print count7 
print count6
print count5 
print count4 
print count3 
print count2 
print count1  

plt.figure()
venn3(subsets=(count1,count2,count6,count3,count4,count6,count7), set_labels = ('SuHW','CTCF','BEAF'))
plt.savefig("Union Venn Diadram.png")
plt.show()