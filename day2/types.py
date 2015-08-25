#!/usr/bin/env python 

#Use four spaces, not a tab when coding! 

# Integer unlimited 
i = 10000 

# Floating point / real number 
f = 0.333

#Converting from integer to float 
i_as_f = float(i)
f_as_i = int(f)

# String -- can have double quote or single quote 
s = "A String" 

#Boolean 
truthy = True 
falsy = False 

# Lists -- convention contains only one type 
l = [1,2,3,4,5]
l.append(7)

# tuple are immutable (cannot be changed) -- the elements can have different types 
t = (1,"foo",5.0)

# Dictionary 
d1 = { "key1": "value1", "key2": "value2" }
d2 = dict( key1="value1", key2="value2" )
d3 = dict( [ ("key1", "value1"), ("key2", "value2") ] )

for value in ( i, f, s, truthy, l, t, d1, d2, d3 ):
        print value, type( value )

