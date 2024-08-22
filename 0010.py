#!/usr/bin/env python3

from math import sqrt


def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit

    isqrt = int(sqrt(limit))
    for i in range(2, isqrt):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    return [i for i in range(2, limit) if is_prime[i]]


s = sum(sieve_of_eratosthenes(2_000_000))

print(s)
