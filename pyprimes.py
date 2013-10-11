# coding: utf-8

import collections
import numpy


def numpy_primes(limit):
    """Generate prime numbers less than limit.

    Use Sieve of Eratosthenes. Assume limit > 2
    """
    yield 2
    is_prime = numpy.ones(limit, dtype=numpy.bool)
    for n in xrange(3, int(limit**.5)+1, 2):
        if is_prime[n]:
            yield n
            is_prime[n*n::n] = False
    for n in xrange(n+2, limit, 2):
        if is_prime[n]:
            yield n


def factors(number):
    factors_list = []
    d = 2
    while number > 1:
        while number % d == 0:
            factors_list.append(d)
            number /= d
        d += 1
        if d * d > number:
            if number > 1:
                factors_list.append(number)
            break
    return factors_list


def numbers_with_n_factors(n):
    i = 2
    while 1:
        fact = collections.Counter(factors(i))
        if len(fact.keys()) == n:
            yield i, fact
        i += 1


def primes(n):
    gen = numbers_with_n_factors(1)
    while n > 0:
        number = gen.next()
        if number[1].values() == [1]:
            yield number[0]
            n -= 1


def nth_prime(nth):
    gen = primes(nth)
    for i in xrange(nth - 1):
        gen.next()

    return gen.next()


def isPrime(n):
    """
    Smart trial division optimized
    Returns True if n is prime
    """
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False

    for f in xrange(5, int(n ** .5) + 1, 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False

    return True


def sieve(n):
    m = (n - 1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p * p < n:
        if b[i]:
            ps.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b[j] = False
                j = j + 2 * i + 3
        i += 1
        p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1
        p += 2
    return ps