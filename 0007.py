#!/usr/bin/env python3

from math import log, sqrt

# See https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime
def upper_bound_for_p_n(n):
    if n < 6:
        return 20
    return int(n * (log(n) + log(log(n))))


def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit

    isqrt = int(sqrt(limit))
    for i in range(2, isqrt):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    return [i for i in range(2, limit) if is_prime[i]]


l = upper_bound_for_p_n(10_001)
p = sieve_of_eratosthenes(l)
n = p[10_001 - 1]  # zero-based array

print(n)
