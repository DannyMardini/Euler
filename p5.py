#! /usr/bin/env python
def SmallestMultiple(n):
    primeFactors = []
    SmallestMultiple = 1

    for i in range(1, n+1):
        for prime in primeFactors:
            if i % prime == 0:
                i = i / prime
        if i > 1:
            primeFactors.append(i);

    for prime in primeFactors:
        SmallestMultiple *= prime;

    return SmallestMultiple

