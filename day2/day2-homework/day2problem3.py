#!/usr/bin/env python 

import pandas as pd 

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"
df = pd.read_csv(annotation)

for x in df['sample']:
    
    variable = pd.read_table("/Users/cmdb/qbb2015/stringtie/" + x + "/t_data.ctab")
    roi = variable['t_name'].str.contains('FBtr0331261')
    print variable[roi]
    
