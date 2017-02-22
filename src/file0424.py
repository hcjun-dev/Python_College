# Hyungchol Jun
# 2014-04-24
# P_11.25.py

'''
the recursive computation of Fibonacci numbers can be speeded up significantly by keeping track of the values that have
already been computed. Provide an implementation of the fib function that uses this strategy. Whenever you return a new
value, also store it an auxiliary list(dictionary). However, before embarking on a computation, consult the list to find
whether the result has already been computed. Compare the running time of your improved implementation with that of the
original recursive implementation and the loop implementation.
'''


def fib(inputV):
	randic = {}
	if inputV < 2:
		return inputV
	else:
		r = (fib(inputV - 1) + fib(inputV - 2))
		randic[fib(inputV - 1)] = fib(inputV - 1)
		randic[fib(inputV - 2)] = fib(inputV - 2)
		return r


def func0424():
	print(fib(9))  # sample input

