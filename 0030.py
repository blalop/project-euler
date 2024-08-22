#!/usr/bin/env python3

s = 0

for i in range(1, 5 * (9**5)):
    if len(str(i)) > 1 and sum([int(j) ** 5 for j in str(i)]) == i:
        s += i

print(s)
