def sumEvenFib(n):
	sum = 0
	a, b = 0, 1
	while a <= n:
		print a
		if (a%2 == 0):
			sum += a
		a,b = b,a+b
	
	print "Sum of all even numbers:",sum
