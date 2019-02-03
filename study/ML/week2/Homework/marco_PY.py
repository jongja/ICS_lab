memo = {1:1, 2:1}		# memo is object!!!

def Fibonacci(n):		# good but memory complex is O(n)
	if n == 0:		# Fibo(0) = 0
		return 0

	if n not in memo:	# if memo has not key n
		memo[n] = Fibonacci(n-1) + Fibonacci(n-2)	# insert dictionary the key:value

	return memo[n]		# if key exist in memo(dictionary)... return value.

print(Fibonacci(50))


def fibo(n):
	a, b = 1, 0		# fibo(1)=1, fibo(0)=0
	for i in range(n):	# 
		a, b = b, a+b   # swap,,!
	return b

print(Fibonacci(50))

