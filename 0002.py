#!/usr/bin/env python3


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


s = sum([i for i in fibonacci(4_000_000) if i % 2 == 0])
print(s)
