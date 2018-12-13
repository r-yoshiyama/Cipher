#!/usr/bin/env python
# coding:utf-8

'''
lehman.py
author : yopiyama

lehman is prime factorization algorithm
'''

import math

def lehman(N):
    for d in range(2, int(pow(N, 1/3) + 1)):
        if N % d == 0:
            return d
    for k in range(1, int(pow(N, 1/3))):
        for a in range(math.ceil(2 * math.sqrt(k*N)),math.floor(2 * math.sqrt(k*N)+pow(N, 1/6)/(4 * math.sqrt(k)))):
            if type(sqrt(a**2 - 4*k*N)) is int:
                return math.gcd(a+b, N)
    return N

def main():
    N = int(input("number >>> "))
    print(lehman(N))

if __name__ == "__main__":
    main()
