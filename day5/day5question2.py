#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import sys 
from blastscore import BLASTScore 

reader = BLASTScore(sys.argv[1])

list1 = []
list2 = []
for i, (score, evalu) in enumerate(reader):
    list1.append(float(score))
    list2.append(float(evalu))
    

#plt.figure()
#plt.hist(list1, bins = (50,100,150,200,250,300,350,400), log = False, range = (0, 200))
#plt.xlabel("Log of FPKM")
#plt.ylabel("Frequency")
#plt.title("Alignment Scores")
#plt.savefig("AlignmentScores.png")

plt.figure()
plt.hist(list2, bins = 10)
plt.xlabel("Log of FPKM")
plt.ylabel("Frequency")
plt.title("E-Values")
plt.savefig("E-values Histogram.png")

#plt.figure()
#plt.scatter((np.log10(list1)), (np.log10(list2)))
#plt.xlabel("Data distribution")
#plt.ylabel("Log2-fold difference")
#plt.title("Scatterplot of Scores and E-values")
#plt.savefig("ScatterplotofScoresandEval.png")


