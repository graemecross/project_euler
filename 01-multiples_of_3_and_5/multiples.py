#!/usr/bin/env python3
"""
Project Euler Problem 1:
Multiples of 3 and 5

https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples_5_3(n):
    """
    Calcultates the sum of all the natural numbers below 10
    that are multiples of 3 or 5.

    We have to subtract the sum of multiples of 15 to avoid duplicates
    """
    return (sum_of_multiples(n, 3) +
            sum_of_multiples(n, 5) -
            sum_of_multiples(n, 15))


def sum_of_multiples(n, m):
    """
    the sum of integers from 1 to n is 0.5*n*(n+1)
    for the multiples we can take out a factor of m and sum from 1 to n/m
    """
    x = (n - 1) // m
    return int(0.5 * x * m * (x + 1))


print(sum_of_multiples_5_3(1000))
