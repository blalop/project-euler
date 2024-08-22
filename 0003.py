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


n = 600851475143
primes = sieve_of_eratosthenes(int(sqrt(n)))
s = 0

while n > 1:
    for prime in primes:
        if n % prime == 0:
            n //= prime
            s = max(s, prime)

print(s)
