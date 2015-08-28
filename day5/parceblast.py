#!/usr/bin/env python

"""
Parse a single BLAST file from stdin and print it 
"""

import sys 
from blastreader import BLASTReader

reader = BLASTReader(sys.argv[1])

#while 1:
#    print reader.next()

for i, (ident, seq) in enumerate (reader):
    print i, ident, seq 

