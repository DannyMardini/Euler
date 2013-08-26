#!/usr/bin/env python
from math import sqrt

def isPrime(n):
    #0 and 1 are not prime numbers.
    if n == 1 or n == 0:
        return False

    num = 2
    while num != n:
        if (n%num == 0):
            return False
        num += 1

    return True

def getNextPrime(n):
	while True:
		n = n+1 if (n%2 == 0 or n <=2) else n+2
		if isPrime(n):
			return n
			
def largestPrimeFactor(n):
	currPrime = 2
	while n > 1:
		if (n % currPrime == 0):
			n = n/currPrime
		else:
		#currPrime = getNextPrime(currPrime)
			currPrime += 1

	return currPrime

# This works because all prime numbers are the building blocks of ever other number, so if we just
# incrementally divide by the number we will get all the prime factors of it and the last one will
# be the greatest prime factor.
def yanzqSolution(a):
	i = 2

	while (a != 1):
		while(a%i != 0):
			i+=1
		print "Factor:",i
		a=a/i
	
	return i
