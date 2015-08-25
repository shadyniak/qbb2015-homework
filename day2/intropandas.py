#!/usr/bin/env python 

import pandas as pd 

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

# print df 
# print df.head() 

# print df.describe() ### prints statistics 
# print df.info() 

#print "\nthis is what happens with [1:5}\n"
#print df[1:5] #the last number is not included) 

#show rows 10 through 15 (1-based, inclusive)
#print def [9:15]
#show rows 20 through 25 
#print df[19:25]

#print df.info()
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]
#print df.info()

#print df.sort("type", ascending=False)
#print df.soirt(ascending=False, columns="type")

#print df["chromosomes"]

#subset chromosome, start and end 
#print df [["chromosome", "start", "end"]]

#subset by row and column 

#print df ["start"][9:15]

#print df.shape 
#df2 = df["start"]
#print df2.shape 

#df2.to_csv("startcolumn.txt", sep='\t', index=False)

#print df.shape
roi = df["start"] < 10 #cannot use for strings, only numerical operations 
#print roi.shape 
#print df[roi]
#print df[roi].shape  

 



