#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import pylab as p 

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab") 

mean = np.mean(df["FPKM"])
stddev = np.std(df["FPKM"])

#mu, sigma = 
x = mean + stddev * p.randn(10000)

#mean = 13.4813251272 
#stddev = 88.6996601083

n, bins, patches = p.hist(x, 50, normed=1, histtype='stepfilled')
p.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

y = p.normpdf(bins, mean, stddev)

plt.figure()
plt.plot(bins,  y, 'k--', linewidth = 1.5)
plt.savefig("density.png")