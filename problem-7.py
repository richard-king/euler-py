#!/usr/bin/python

primes = [2, 3, 5, 7, 11, 13]
candidate = 17

while len(primes) < 10001 :
   prime = True
   for i in (z for z in primes if z**2 <= candidate) :
      if not candidate % i :
	 prime = False
	 break
   if prime :
      primes.append(candidate)
   candidate += 2
else :
   print primes.pop()
