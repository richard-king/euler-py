#!/usr/bin/python

for a in xrange (1, 332) :
   for b in xrange (a, (1000 - a) / 2) :
      c = 1000 - (a + b)
      if a**2 + b**2 == c**2 : 
	 print a * b * c
