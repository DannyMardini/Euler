#!/usr/bin/env python

def nthPrime(n):
    i = 2
    primes = [i]

    while len(primes) < n:
        i += 1
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    return primes.pop()
