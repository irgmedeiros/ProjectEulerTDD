# coding: utf-8

"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiple(numero, multiplo):
    return numero % multiplo == 0


def multiples(numero, *multiplos):
    for testnum in xrange(1, numero + 1):
        for m in multiplos:
            if multiple(testnum, m):
                yield testnum
                break

