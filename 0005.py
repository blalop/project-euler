#!/usr/bin/env python3

n = 0
while True:
    n += 20
    if (
        n % 11 == 0
        and n % 12 == 0
        and n % 13 == 0
        and n % 14 == 0
        and n % 15 == 0
        and n % 16 == 0
        and n % 17 == 0
        and n % 18 == 0
        and n % 19 == 0
    ):
        break

print(n)
