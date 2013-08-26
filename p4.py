#! /usr/bin/env python
def reverseString(str):
	newStr = ""
	for c in str:
		newStr = c + newStr
	
	return newStr

def isPalindrome(n):
	nStr = str(n)
	if nStr == nStr[::-1]:
		return True
	else:
		return False

def largestPalindrome():
	pA = 999
	maxPalindrome = 0
	maxA = 0
	maxB = 0
	
	while pA >= 100:
		pB = 999
		while pB >= 100:
			product = pA * pB
			if isPalindrome(product):
				if product > maxPalindrome:
					maxPalindrome = product
					maxA = pA
					maxB = pB

			pB = pB - 1
		
		pA = pA - 1
	
	print "Factors:", maxA, maxB
	return maxPalindrome