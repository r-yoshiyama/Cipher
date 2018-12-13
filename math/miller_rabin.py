#!/usr/bin/env python
# coding:utf-8

"""
Miller Rabin Primality Test
"""

import random

def is_prime(n, k=30):
    """
    is_prime function
    Implemented with Miller Rabin.

    Parameters
    ----------
    n : int
        Number that
    k : int
        max loop count, default = 30

    Returns
    -------
    True/False : boolean
        if n is prime return True, else return False
    """

    assert type(n) is int, "This function's argument is INT only"

    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(k):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1
        if y != n - 1 and t & 1 == 0:
            return False
    return True

def main():
    """ Main function """
    import sys
    n = int(sys.argv[1])
    try:
        k = int(sys.argv[2])
    except IndexError:
        k = 30
    ans = is_prime(n, k)
    if ans:
        print("{0} is Prime Number".format(n))
    else:
        print("{0} is Composite Number".format(n))

if __name__ == "__main__":
    main()
