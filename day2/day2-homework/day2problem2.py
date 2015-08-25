#!/usr/bin/env python 

import pandas as pd 
import matplotlib.pyplot as plt 

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

subset = df[df['type'].str.contains("transcript")]
subset2 = subset[subset["attributes"].str.contains("FBgn0264270")]

#Sxl FBgn0264270 gene id 
roi = df["attributes"].str.contains("FBgn0264270")

plt.figure()
plt.plot(subset2["start"])
plt.xlabel("Gene")
plt.ylabel("Start Position")
plt.title("Sxl")
plt.savefig("startsSxlsubset2.png")

