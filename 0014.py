#!/usr/bin/env python3

sn = 0
sc = 0

for i in range(2, 1_000_000):
    n = i
    c = 0
    while n != 1:
        if n % 2 == 0: n = n // 2
        else: n = 3 * n + 1
        c = c + 1
    
    
    if c > sc:
        sc = c
        sn = i

print (sn)