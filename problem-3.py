#!/usr/bin/python

import math

def naive_prime_test(n) :
	for i in xrange(2, int(math.floor(math.sqrt(n))) + 1) :
		if not n%i :
			return False
	return True

big_num = 600851475143
big_num_root = int(math.floor(math.sqrt(big_num)))

factors = reversed([x for x in xrange(2, big_num_root + 1) if not big_num % x])

for f in factors :
	if naive_prime_test(f) :
		print f
		break
