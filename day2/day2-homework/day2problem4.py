#!/usr/bin/env python 

import pandas as pd 
import matplotlib.pyplot as plt 

plot = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = plot["FPKM"] >0

plot2 = plot[roi]["FPKM"]

firstthird = plot2[0:3182]
secondthird = plot2[3182:6365]
thirdthird = plot2[6365:9548]

plt.figure()
plt.boxplot([firstthird, secondthird, thirdthird])
plt.xlabel("gene")
plt.ylabel("position on the chromosome")
plt.title("Boxplot of FPKM values")
plt.savefig("BoxplotFPKM.png")
