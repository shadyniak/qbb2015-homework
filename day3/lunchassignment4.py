#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import pylab as p 

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab") 
df2 = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072894/t_data.ctab") 

R = df["FPKM"]
G = df2["FPKM"]

M = np.log2(R/G)
A = 0.5 * np.log2(R * G)

plt.figure()
plt.scatter(A, M)
plt.xlabel("Data distribution")
plt.ylabel("Log2-fold difference")
plt.title("Comparison MA plot")
plt.savefig("MA.png")