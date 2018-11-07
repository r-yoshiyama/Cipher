#!/usr/bin/env python
#coding:utf-8

"""
This is RSA's generate, encode and decode script writen in python.
author = Ryota Yoshiyama
Last Update = 27/10/17 16:04:13
"""


import random
import time

def check(a, s, d, n):
	""" Miller Rabin Check """
	x = pow(a, d, n)
	if x == 1:
		return True
	for i in range(s - 1):
		if x == n - 1:
			return True
		x = pow(x, 2, n)
	return x == n - 1

def isPrime(p):
	""" return True if p is Prime """
	k = 30
	if p == 2:
		return True
	if not p & 1:
		return False
	s = 0
	d = p - 1
	while d % 2 == 0:
		d >>= 1
		s += 1
	for i in range(k):
		a = random.randint(2, p - 1)
		if not check(a, s, d, p):
			return False
	return True

def primeGene(N):
	p = 4
	l = 10
	b = random.randint(0, pow(2, N-l-1)-1)
	while not isPrime(p):
		a = random.randint(0, pow(2, l) - 1)
		p = pow(2, N - l) * a + 2 * b + 1
	return p

def ex_euclid(a,b):
	a0, x0, y0 = a, 1, 0
	a1, x1, y1 = b % a, 0, 1
	while a1 != 0:
		q = a0 // a1
		a0, x0, y0, a1, x1, y1 = a1, x1, y1, a0 - q * a1, x0 - q * x1, y0 - q * y1
	return y0 % a

def gen(bit = 3072):
	""" Generate Keys Function """
	p, q = primeGene(bit//2), primeGene(bit//2)
	N = p * q
	e = 65537
	phi = (p - 1)*(q - 1)
	d = ex_euclid(phi, e)
	# f = open("text_rsa.txt", "a")
	# star = "*"*80
	# text = "\nPublic key pair(N, e)\nN = {0}\n\ne = {1}\n\nSecret key d\n{2}\n".format(N, e, d)
	# f.write("\n"+star+text+star+"\n")
	# f.close()
	return N, e, d

def enc(m, e, N):
	""" Encode Function """
	c = pow(m, e, N)
	# print(c)
	# f = open("text_rsa.txt", "a")
	# f.write("\n" + "-"*80 + "\ncipher text\n" + str(c) + "\n" + "-"*80 + "\n")
	# f.close()
	return c

def dec(c, d, N):
	"""Decode Function """
	m = pow(c, d, N)
#	f = open("text_rsa.txt", "a")
#	f.write("\n" + "+"*80 + "\nplane text\n" + str(m) + "\n" + "+"*80 + "\n")
#	f.close()
	# print(m)
	return m

def main():
	""" Main Function """
	m = 1234567890
	N, e, d = gen(3072)
	start_time = time.time()
	c = enc(m, e, N)
	m = dec(c, d, N)
	exec_time = time.time() - start_time
	print("{0}".format(exec_time))


if __name__ == "__main__":
	main()
