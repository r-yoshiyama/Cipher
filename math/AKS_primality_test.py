#!/usr/bin/env python
# coding:utf-8

"""
AKS Primality Test
"""
import math

def phi(r):
    """ tortient function """
    prime_fact_list = []
    n = r
    for p in range(2, int(math.sqrt(r)) + 1):
        while n % p == 0:
            prime_fact_list.append(p)
            n /= p
    phi_r = r
    for p in prime_fact_list:
        phi_r *= (1 - (1/p))
    return phi_r

def find_enough_order(n):
    """ Find the smallest r such that o_r(n) > (log2 n)2 """
    log_n_2 = math.log2(n) ** 2
    for r in range(1, n):
        if math.gcd(r, n) == 1:
            order = -1
            # n^e mod r
            ne_r = 1
            for e in range(1, r):
                ne_r = ne_r * n % r
                if ne_r == 1:
                    order = e
                    break
            if order > log_n_2:
                return r
        else:
            continue
    return n

def is_prime(n):
    """ AKS Function if n is prime, return True. else if n is composite, return False"""
    assert type(n) is int, "This function's argument is INT only"

    # Step 1
    # n = a^b
    for b in range(2, int(math.log2(n) + 1)):
        a = n ** (1 / b)
        if (a - math.floor(a)) == 0:
            return False

    # Step 2
    # o_r (n) > 4 log n
    # Find the smallest r such that o_r(n) > (log2 n)2
    log_n_2 = math.log2(n) ** 2
    for r in range(1, n):
        if math.gcd(r, n) == 1:
            order = -1
            # n^e mod r
            ne_r = 1
            for e in range(1, r):
                ne_r = ne_r * n % r
                if ne_r == 1:
                    order = e
                    break
            if order > log_n_2:
                break
        else:
            continue
    if order <= log_n_2:
        r = n

    # Step 3
    # Simple Primality Test
    for a in range(2, min(r + 1, n)):
        if n % a == 0:
            return False

    if n <= r:
        return True

    # Step 4 Unimplemented
    for a in range(1, int(math.sqrt(phi(r)) * math.log(n)) + 1):
        a

    # Step 5 Unimplemented

def main():
    """ Main function """
    import sys
    n = int(sys.argv[1])

    ans = is_prime(n)
    if ans:
        print("{0} is Prime Number".format(n))
    else:
        print("{0} is Composite Number".format(n))

if __name__ == "__main__":
    main()
