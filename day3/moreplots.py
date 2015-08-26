#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt 

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
metadata2 = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

Sxlf = []
Sxlm = []
Sxlrm = []
Sxlrf = []

for samplef in metadata[metadata["sex"] == "female"]["sample"]:
    dff = pd.read_table("~/qbb2015/stringtie/" + samplef + "/t_data.ctab")
    roif = dff["t_name"].str.contains("FBtr0331261")
    Sxlf.append(dff[roif]["FPKM"].values)

for samplem in metadata[metadata["sex"] == "male"]["sample"]:
    dfm = pd.read_table("~/qbb2015/stringtie/" + samplem + "/t_data.ctab")
    roim = dfm["t_name"].str.contains("FBtr0331261")
    Sxlm.append(dfm[roim]["FPKM"].values)
    
for replicatesm in metadata2[metadata2["sex"] == "male"]["sample"]:
    dfrm = pd.read_table("~/qbb2015/stringtie/" + replicatesm + "/t_data.ctab")
    roirm = dfrm["t_name"].str.contains("FBtr0331261")
    Sxlrm.append(dfrm[roirm]["FPKM"].values)
    
for replicatesf in metadata2[metadata2["sex"] == "female"]["sample"]:
    dfrf = pd.read_table("~/qbb2015/stringtie/" + replicatesf + "/t_data.ctab")
    roirf = dfrf["t_name"].str.contains("FBtr0331261")
    Sxlrf.append(dfrf[roirf]["FPKM"].values)
    
plt.figure()
plt.plot(Sxlf, 'r', label = "Female")
plt.plot(Sxlm, 'b', label = "Male")
plt.plot([4,5,6,7], Sxlrm, 'go', label = "Replicates Male")
plt.plot([4,5,6,7], Sxlrf, 'yo', label = "Replicates Female")
plt.legend(loc = 'upper left')
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt. ylim((0, 300))
plt.title("Sxl")
plt.xticks(range(len(Sxlm)),["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation=90)
plt.savefig("timecourse.png") 

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

plt.figure()
plt.scatter(df["FPKM"], df2["FPKM"])
plt.xlabel("893 - male 10")
plt.ylabel("915 - female 14D")
plt.savefig("scatterplot.png")

chromosomes = {} 

for i, line in df.iterrows():
    if line["chr"] in ["2L", "2R", "3L", "3R", "X", "Y"]:
        if line["chr"] not in chromosomes:
            chromosomes [line["chr"]] = 1 
        else:
            chromosomes [line["chr"]] += 1 

plt.figure()
plt.bar(left = range(len(chromosomes)), height = chromosomes.values()) 
plt.xticks(range(len(chromosomes)), chromosomes.keys()) 
plt.savefig("barplot.png")




