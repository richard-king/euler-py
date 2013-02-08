#!/usr/bin/python

import fractions

def lcm(a, b) :
	return (a * b) / fractions.gcd(a, b)

total = 1

for i in xrange(11, 21) :
	total = lcm(total, i)

print total
