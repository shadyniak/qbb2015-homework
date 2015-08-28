#!/usr/bin/env python

from __future__ import division 
import sys
import chrombits

arr = chrombits.ChromosomeLocationBitArrays(fname = sys.argv[1])

A = arr.copy()
B = arr.copy()

A.set_bits_from_file(sys.argv[2])
B.set_bits_from_file(sys.argv[3])

new = A.intersect(B.complement())
thing = new.bed()
print thing