#!/usr/bin/env python3

from math import factorial

f = factorial(100)
s = sum([int(d) for d in str(f)])

print(s)
