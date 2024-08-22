#!/usr/bin/env python3

from math import inf


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


s = 0
for i, n in enumerate(fibonacci(inf)):
    if len(str(n)) == 10**3:
        s = i
        break

print(s)
