#!/usr/bin/env python3

sum_of_squares = sum([i**2 for i in range(101)])
square_of_sum = sum([i for i in range(101)]) ** 2

d = square_of_sum - sum_of_squares
print(d)
