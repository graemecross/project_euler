# Project Euler Problem 1

## [Multiples of 3 and 5](https://projecteuler.net/problem=1)

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Comments on Solution

Initially, one could think of the simple approach of looping over all the numbers from 1 to 1000, check if the number is a multiple of 3 or 5 and add it to a running total.

There is, however, a more optimal solution.

The sum of all natural numbers from 1 to n is:

![equation](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Cfrac%7Bn%28n&plus;1%29%7D%7B2%7D)

Therefore, in the sum of multiples (*m + 2m + 3m + ... + n*), *m* can be factored out to give *m*(*1 + 2 + 3 + ... + n/m*)

If we do this process for both *m = 3* and *m = 5*, we get an overlap of when the number is both a factor of *3* and *5*. Because of this, we must subtract those multiples in the form of the same calculation, a third time for factors of *15*.

This second approach gives a solution that is *O(1)* in contrast to the initial naive approach, which is *O(n)*.

## Choice of Language

In this solution, I have chosen to use Python. This solution is a simple calculation and as such, would be relatively simple to implement in most programming languages.