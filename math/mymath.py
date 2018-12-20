#! user/bin/env python3
# codingg: utf-8

"""
My Math package
"""

import math
import random


def ex_euclid(a, b):
    """
    Extended Euclidean algorithm
    a * x + b * y = gcd(a, b)

    Parameters
    ----------
    a : INT
        a
    b : INT
        b
    Returns
    -------
    y : INT
        y
    """

    a0, x0, y0 = a, 1, 0
    a1, x1, y1 = b % a, 0, 1
    while a1 != 0:
        q = a0 // a1
        a0, x0, y0, a1, x1, y1 = a1, x1, y1, a0 - q * a1, x0 - q * x1, y0 - q * y1
    return y0 % a


def lehman(N):
    """
    Lehman Factorization algorithm

    Parameters
    ----------
    N : INT
        target number
    Returns
    -------
    - : INT
        return_var_description
    """

    for d in range(2, int(pow(N, 1/3) + 1)):
        if N % d == 0:
            return d
    for k in range(1, int(pow(N, 1/3))):
        start = math.ceil(2 * math.sqrt(k*N))
        end = math.floor(2 * math.sqrt(k*N)+pow(N, 1/6)/(4 * math.sqrt(k)))
        for a in range(start, end):
            b = math.sqrt(a**2 - 4*k*N)
            if isinstance(b, int):
                return math.gcd(a + b, N)
    return N


def is_prime(n, k=30):
    """
    is_prime module
    Implemented with Miller Rabin.

    Parameters
    ----------
    n : INT
        Number that
    k : INT
        max loop count, default = 30
    Returns
    -------
    True/False : boolean
        if n is prime return True, else return False
    """
    warn_str = "This function's argument is INT only"
    assert isinstance(n, int), warn_str + " n : not INT"
    assert isinstance(k, int), warn_str + " k : not INT"

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
    """
    main method for test operation of function

    Parameters
    ----------
    none
    """
    n = 191

    print(is_prime(n))
    print(lehman(n))


if __name__ == "__main__":
    main()
