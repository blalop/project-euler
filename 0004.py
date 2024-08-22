#!/usr/bin/env python3

p = [i * j for i in range(1000) for j in range(1000) if str(i * j) == str(i * j)[::-1]]
m = max(p)

print(m)
