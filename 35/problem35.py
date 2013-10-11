# coding: utf-8

#import itertools
import pyprimes
from collections import deque


def circular_primes(num):
    """Get all the circular primes up to :num:"""

    primes = list(pyprimes.numpy_primes(num))

    for prime in primes:
        circular = True
        rotator = deque(str(prime))

        for _i in xrange(len(str(prime) - 1)):
            rotator.rotate()
            n = int(''.join(map(str, list(rotator))))
            if n not in primes:
                circular = False
                break

        if circular:
            yield prime
