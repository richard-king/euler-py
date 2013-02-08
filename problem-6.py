#!/usr/bin/python

sum_of_squares = sum([x**2 for x in xrange(0,101)])
square_of_sum = sum(xrange(0,101))**2

print square_of_sum - sum_of_squares
