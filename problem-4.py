#!/usr/bin/python

def palindrome(n) :
	return str(n) == str(n)[::-1]

leader = 0

for i in xrange(100,1000) :
	for j in xrange(100,1000) :
		if i * j > leader and palindrome(i * j) :
			leader = i * j

print leader
