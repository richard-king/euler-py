#!/usr/bin/python

def fibonacci(i) :
   if i in range(0,2) :
      return i
   else :
      p = 0
      q = 1
      for j in range(2, i+1) :
	 r = q + p
	 p = q
	 q = r
      return r

n = 0
z = 1

while fibonacci(z) < 4000000 :
   if not fibonacci(z)%2 :
      n += fibonacci(z)
   z += 1

print n
