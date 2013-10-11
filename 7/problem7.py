# coding: utf-8
import collections


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