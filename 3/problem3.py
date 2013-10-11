# coding: utf-8


# Sieve of Eratosthenes
def primes_less_than(number):
    primes = set([2])  # primes set starting with 2
    primes_candidates = {x for x in xrange(3, number, 2)}  # odd numbers from 3 to number
    while primes_candidates:
        candidate = min(primes_candidates)
        primes.add(candidate)
        primes_candidates.difference_update(xrange(candidate, number, candidate))

    return primes


def factors(number):
    factors_set = set()
    d = 2
    while number > 1:
        while number % d == 0:
            factors_set.add(d)
            number /= d
        d += 1
        if d * d > number:
            if number > 1:
                factors_set.add(number)
            break
    return factors_set


def largest_prime_factor(number):
    return max(factors(number))
