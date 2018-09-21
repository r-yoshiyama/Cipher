#!/usr/bin/env python
# coding:utf-8

'''
miller_rabin.py
author:yopiyama
Miller Rabin is primality test.
'''

import random

def miller_rabin(n, k = 30):
	# assert type(n) != int, "This function's argument is INT only"

	if n == 2:
		return True
	elif ~ n & 1:
		return False

	s = 0
	d = n - 1
	while ~d & 1:
		d >>= 1
		s += 1
	for i in range(k):
		a = random.randint(2,n - 1)
		if not check(a, s, d, n):
			return False
	return True

def check(a, s, d, n):
	x = pow(a, d, n)
	if x == 1:
		return True
	for i in range(s - 1):
		if x == n-1:
			return True
		x = pow(x, 2, n)
	return x == n-1

def main():
	import sys
	n = int(sys.argv[1])
	try:
		k = int(sys.argv[2])
	except IndexError:
		k = 30
	ans = miller_rabin(n, k)
	if ans:
		print("{0} is Prime Number".format(n))
	else:
		print("{0} is Composite Number".format(n))

if __name__ == "__main__":
	main()
