#! /usr/bin/env python

def SumSquareDiff(n):
    sumOfSquares = 0
    squareOfSums = 0

    for i in range(1,n+1):
        sumOfSquares += (i*i)
        squareOfSums += i

    squareOfSums *= squareOfSums

    return squareOfSums - sumOfSquares
