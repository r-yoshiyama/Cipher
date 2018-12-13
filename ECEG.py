#!/usr/bin/env python
#coding:utf-8

"""
This is Elliptic Curve ElGamal Cryptography's generate, encode and decode script writen in python.
Author = Ryota Yoshiyama
Last Update = Wed., Aug. 01 , 2018
"""

import binascii
import copy
import random
import time
import numpy as np

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

def primeGene(N):
    """
    Prime Generator

    Parameters
    ----------
    N : int
        bit size

    Returns
    -------
    p : int
        Random Prime Number (N bit)
    """

    p = 4
    l = 10
    b = random.randint(0, pow(2, N-l-1)-1)
    while not is_prime(p):
        a = random.randint(0, pow(2, l) - 1)
        p = pow(2, N - l) * a + 2 * b + 1
    return p

def ex_euclid(a, b):
    """
    Euclidean algorithm
    ax + by = 1

    Parameters
    ----------
    a : int
        a
    b : int
        b

    Returns
    -------
    y0%a : int
        y
    """

    a0, x0, y0 = a, 1, 0
    a1, x1, y1 = b%a, 0, 1
    while a1 != 0:
        q = a0 // a1
        a0, x0, y0, a1, x1, y1 = a1, x1, y1, a0 - q * a1, x0 - q * x1, y0 - q * y1
    return y0 % a

def two_times_point(point, a, p):
    """
    Scalar Multiplication (To double Point ) on Elliptic Curve
    2 * (x, y) = (xn, yn)

    Parameters
    ----------
    point : list
        Target Point
    a : int
        Elliptic Curve parameter
    p : int
        Elliptic Curve parameter, modulo

    Returns
    -------
    [xn, yn] : list
        (xn, yn) = 2 * (x, y)
    """
    x = point[0]
    y = point[1]
    tmp = ex_euclid(p, 2*y)
    l = ((3 * x**2 + a)* tmp)%p
    xn = (l**2 - 2 * x)%p
    yn = (l * (x - xn) - y)%p
    return [xn, yn]

def add_point(point0, point1, p):
    """
    Point Addition on Elliptic Curve
    (x0, y0) + (x1, y1) = (xn, yn)

    Parameters
    ----------
    point0 : list
        (x0, y0)
    point1 : int
        (x1, y1)
    p : int
        Elliptic Curve parameter, modulo

    Returns
    -------
    [xn, yn] : list
        (xn, yn) = (x0, y0) + (x1, y1)
    """
    x0, y0 = point0[0], point0[1]
    x1, y1 = point1[0], point1[1]

    tmp = ex_euclid(p, x1 - x0)
    l = ((y1 - y0)* tmp)%p
    xn = (l**2 - x1 - x0)%p
    yn = (l * (x0 - xn) - y0)%p
    return [xn, yn]

def k_times_point(k, point, a, p):
    """
    Scalar Multiplication on Elliptic Curve
    k * (x, y) = (qx, qy)

    Parameters
    ----------
    k : int
        Number multiplied
    point : list
        Target Point
    a : int
        Elliptic Curve parameter
    p : int
        Elliptic Curve parameter, modulo

    Returns
    -------
    point_q : list
        Result, (qx, qy)
    """

    d = format(k, "b")
    point_q = copy.deepcopy(point)
    d = d[1:]
    for i in d:
        point_q = two_times_point(point_q, a, p)
        if i == "1":
            point_q = add_point(point, point_q, p)
    return point_q


def gen():
    """
    GF(p)上の楕円曲線E(F_p)および，それの有理点P_g(生成元)を選ぶ．
    P_gの位数をqとする．次にx \in Z_qをランダムに選び，P_y = xP_gを計算する．
    最後に，Pk = (E(F_p), P_g, P_y)を公開鍵として公開し，Sk = x を秘密鍵として保存する．
    # 192
    a = -3
    p = 6277101735386680763835789423207666416083908700390324961279
    pgx = int("0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012",16)
    pgy = int("0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811",16)
    q = 6277101735386680763835789423176059013767194773182842284081
    # 224
    a = -3
    p = 26959946667150639794667015087019630673557916260026308143510066298881
    pgx = int("0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21",16)
    pgy = int("0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34",16)
    q = 26959946667150639794667015087019625940457807714424391721682722368061
    # 256
    # a = -3
    # p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    # pgx = int("0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296", 16)
    # pgy = int("0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5", 16)
    # q = 115792089210356248762697446949407573529996955224135760342422259061068512044369
    """

    a = int("0x0000000000000000000000000000000000000000000000000000000000000000", 16)
    b = int("0x0000000000000000000000000000000000000000000000000000000000000007", 16)
    p = int("0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f", 16)
    pgx = int("0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798", 16)
    pgy = int("0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8", 16)
    q = int("0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141", 16)
    x = random.randint(1, q)
    pg = np.array([pgx, pgy])
    py = np.array(k_times_point(x, pg, a, p))

    return pg, py, a, p, q, x


def enc(pg, py, a, p, q, M_text):
    """
    平文 M = (m1, m2) -----(ただし，m1 \in Z_p, m2 \in Z_p)
    適当にr \in Z_qを選び，
    暗号文(Q1, Q2) = (rP_g, M + rP_y) -----(ただし，+はmod p 上の長さ2のベクトルの通常の加算．)
    とする．
    """

    m1 = M_text[:int(len(M_text)/2)]
    m2 = M_text[int(len(M_text)/2):]
    M_bin1 = binascii.hexlify(m1.encode('utf-8'))
    M_bin2 = binascii.hexlify(m2.encode('utf-8'))

    M = np.array([int.from_bytes(M_bin1, "little"), int.from_bytes(M_bin2, "little")])
    r = random.randint(2, q)
    Q1 = np.array(k_times_point(r, pg, a, p))
    Q2 = M + np.array(k_times_point(r, py, a, p))
    return Q1, Q2

def dec(Q1, Q2, x, a, p):
    """
    秘密鍵x暗号文(Q1, Q2)を使い
    M = Q2 - xQ1 (ただし，-はmod p上の長さ2のベクトルの通常の減算)
    を計算する．
    """

    M = Q2 - np.array(k_times_point(x, Q1, a, p))

    m_dec1 = M[0].to_bytes((M[0].bit_length() + 7) // 8, "little")
    m_dec2 = M[1].to_bytes((M[1].bit_length() + 7) // 8, "little")

    return binascii.unhexlify(m_dec1).decode('utf-8') + binascii.unhexlify(m_dec2).decode('utf-8')

def main():
    """
    main method
    """
    start_time = time.time()

    pg, py, a, p, q, x = gen()

    M = "Hello"

    Q1, Q2 = enc(pg, py, a, p, q, M)

    M_dec = dec(Q1, Q2, x, a, p)

    print("Plain text (before encode)) = %s" % M)
    print("Cipher text 1 = [%d, %d]" % (Q1[0], Q1[1]))
    print("Cipher text 2 = [%d, %d]" % (Q2[0], Q2[1]))
    print("Plain text (after decode) = %s" % M_dec)

    exec_time = time.time() - start_time
    print("\nProcess time : {0} sec".format(exec_time))

if __name__ == "__main__":
    main()
