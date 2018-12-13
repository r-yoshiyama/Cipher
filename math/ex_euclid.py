#!/usr/bin/env python
# coding:utf-8

def ex_euclid(a,b):
    a0, x0, y0 = a, 1, 0
    a1, x1, y1 = b % a, 0, 1
    while a1 != 0:
        q = a0 // a1
        a0, x0, y0, a1, x1, y1 = a1, x1, y1, a0 - q * a1, x0 - q * x1, y0 - q * y1
    return y0 % a

def main():
    a, b = map(int,input("p & N >>>").split())
    y = ex_euclid(a, b)
    print(y)

if __name__ == "__main__":
    main()
